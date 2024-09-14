"""
ゲームの実行ファイル。
"""
import sys
import pygame
from   pygame.locals import *
import global_value as glb
import ai_chess
import chess
import game_init
from king import King

def check_king_alive() -> tuple[bool, bool]:
    """
    盤上のキングの生存を確認するメソッド。
    
    --- Returns ---\n
    bool: white_king_alive 白のキングが生存しているかどうか。
    bool: black_king_alive 黒のキングが生存しているかどうか。
    """
    white_king_alive = False
    black_king_alive = False
    for row in chess.c_board.cross_board:
        for piece in row:
            if isinstance(piece, King):
                if piece.iswhite:
                    white_king_alive = piece.alive
                else:
                    black_king_alive = piece.alive
    return white_king_alive, black_king_alive

def display_winner(winner):
    """
    勝者を表示し、ゲームを終了するメソッド。
    
    --- Parameters ---\n
    winner: str 勝者の色。
    """
    font = pygame.font.Font('ipaexg.ttf', 74)
    text = font.render(f"{winner} の勝ち！", True, (255, 255, 255))
    glb.screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす
    glb.screen.blit(text, (400 - text.get_width() // 2, 400 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.wait(3000)  # 3秒待ってゲームを終了する
    pygame.quit()
    sys.exit()

def main():
    # 初期化
    pygame.init()
    glb.screen = pygame.display.set_mode((800, 800))   #windowの作成
    glb.now_white = True
    game_init.init()  #pygemeの初期化を済ませてから呼ぶ
    

    #メインループ
    while True:
        # イベントキューを確認
        glb.olddownflg = glb.downflg    #トリガー用
        for event in pygame.event.get():
            if event.type == QUIT:  # 強制終了
                pygame.quit()       # ゲーム終了時の後始末
                sys.exit()

            # マウス移動イベント
            if event.type == MOUSEMOTION:
                glb.mx, glb.my = event.pos #マウス位置取得

            # マウスボタンイベント
            if event.type == MOUSEBUTTONDOWN:
                glb.downflg = True
                glb.mx, glb.my = event.pos #マウス位置取得
                glb.click_mx = glb.mx   #クリックされた時の場所を保存しておく
                glb.click_my = glb.my

            # マウスボタンイベント
            if event.type == MOUSEBUTTONUP:
                glb.downflg = False
                glb.click_mx = 94       #ボタンが離された時には念のため初期化
                glb.click_my = 89
                glb.mx, glb.my = event.pos #マウス位置取得

        if (glb.now_white and glb.front_white) or (not glb.now_white and not glb.front_white): # プレイヤーの番手
            if glb.downflg:
                if glb.olddownflg:  # ドラッグ
                    pass
                else:   # クリック
                    if 94<=glb.mx<=712 and 89<=glb.my<=708:
                        x = (glb.mx - 94) // chess.B_YOKO_OFF
                        y = (glb.my - 89) // chess.B_TATE_OFF
                        if 0<=x<=7 and 0<=y<=7:
                            if chess.c_board.cross_board[y][x] != 0:
                                chess.c_board.cross_board[y][x].pick = True
                                glb.grab_piece = chess.c_board.cross_board[y][x]
                                glb.grab_piece.pick = True
                    elif 894<=glb.mx<=1512 and 89<=glb.my<=708:
                        x = (glb.mx - 894) // chess.B_YOKO_OFF
                        y = (glb.my - 89) // chess.B_TATE_OFF
                        if 0<=x<=7 and 0<=y<=7:
                            if chess.c_board.cross_board[7-y][7-x] != 0:
                                chess.c_board.cross_board[7-y][7-x].pick = True
                                glb.grab_piece = chess.c_board.cross_board[7-y][7-x]
                                glb.grab_piece.pick = True
            else:
                if glb.olddownflg:  # リリース
                    if 94<=glb.mx<=712 and 89<=glb.my<=708:
                        x = (glb.mx - 94) // chess.B_YOKO_OFF
                        y = (glb.my - 89) // chess.B_TATE_OFF
                        if 0<=x<=7 and 0<=y<=7:
                            if glb.grab_piece.is_moveable(x,y):
                                glb.grab_piece.move(x,y)
                                glb.now_white = not glb.now_white
                    elif 894<=glb.mx<=1512 and 89<=glb.my<=708:
                        x = (glb.mx - 894) // chess.B_YOKO_OFF
                        y = (glb.my - 89) // chess.B_TATE_OFF
                        if 0<=x<=7 and 0<=y<=7:
                            if glb.grab_piece.is_moveable(7-x,7-y):
                                glb.grab_piece.move(7-x,7-y)


                    if glb.grab_piece != 0:
                        glb.grab_piece.pick = False
                    glb.grab_piece = False
        else: # CPUの番手
            if glb.front_white: # CPUは黒（後手）
                movelist = []
                for pi_v in chess.c_board.cross_board:
                    for pi_h in pi_v:
                        if (pi_h != 0) and (not pi_h.iswhite):
                            pi_h.next_move(0, movelist)
                if len(movelist) > 0:
                    max_expected = max(movelist, key=lambda x:x[3])
                    max_expected[0].move(max_expected[2], max_expected[1]) # h, v
            else: # CPUは白（先手）
                movelist = []
                for pi_v in chess.c_board.cross_board: # 駒の描画
                    for pi_h in pi_v:
                        if (pi_h != 0) and (pi_h.iswhite):
                            pi_h.next_move(1, movelist)
                if len(movelist) > 0:
                    max_expected = max(movelist, key=lambda x:x[3])
                    max_expected[0].move(max_expected[2], max_expected[1]) # h, v
            glb.now_white = not glb.now_white
            
            
        glb.screen.fill((0,0,0))  #画面を黒で塗りつぶす
        glb.c_board_inst.draw_board_all()   #ボードの描画
        
        # 描画
        pygame.display.update()  # 画面を更新
        
         # 盤上のキングの生存をチェック
        white_king_alive, black_king_alive = check_king_alive()
        if not white_king_alive: # 黒の勝ち
            pygame.time.wait(1000)
            display_winner("黒")
        elif not black_king_alive: # 白の勝ち
            pygame.time.wait(1000)
            display_winner("白")


if __name__ == '__main__':
    main()