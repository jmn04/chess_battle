import pygame
from   pygame.locals import *
import global_value as glb
import sys

#駒の画像からの切り出し座標
rect_king   = [[158, 0, 38, 91],[  0, 49, 36, 90]]   #[黒のキング,白のキング]
rect_queen  = [[127, 0, 30, 80],[ 39, 66, 30, 80]]   #[黒のクィーン,白のクィーン]
rect_bishop = [[ 93, 0, 30, 70],[ 69, 71, 31, 70]]   #[黒のビショップ,白のビショップ]
rect_knight = [[ 61, 0, 32, 72],[101, 77, 32, 72]]   #[黒のナイト,白のナイト]
rect_rook   = [[ 32, 0, 28, 60],[132, 89, 29, 60]]   #[黒のルーク,白のルーク]
rect_pawn   = [[  8, 0, 25, 46],[161, 93, 25, 46]]   #[黒のポーン,白のポーン]



#チェス盤の座標
B_YOKO_OFF = 77
B_TATE_OFF = 77
VS_HZURE = 114

glb.now_gamewave = 0
glb.grab_piece = False  #盤面につかまれたコマがあれば、その参照を持つ


class c_board:
    """
    チェスボードのクラス。
    """
    cross_board = [[0,0,0,0,0,0,0,0],   #212, 89
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0]]

    def draw_board(self):
        """
        ボードを描画するメソッド。
        """
        glb.screen.blit(glb.img_board, (0,0))

    def draw_board_all(self):
        """
        チェス盤を描画するメソッド。
        """
        glb.screen.blit(glb.img_board, (0,0))

        for pi_v in c_board.cross_board:    #駒の描画
            for pi_h in pi_v:
                if (pi_h != 0) and (pi_h != glb.grab_piece):
                    pi_h.draw_piece(0,0)
        if glb.grab_piece:
            glb.grab_piece.draw_piece(glb.mx-glb.click_mx, glb.my-glb.click_my)


def passage_check(setlist: list, ch_iswhite: int, sv: int, sh: int, delta_v: int, delta_h: int):  #[sv][sh]の次からスタートする
    """
    queen, rook, bisiopの移動判定用メソッド。
    
    --- Parameters ---\n
    setlist: list 移動可能な座標を格納するリスト。
    ch_iswhite: int 0:black, 1:white。
    sv: int 0~7 縦方向の移動元。
    sh: int 0~7 横方向の移動元。
    delta_v: int 縦方向の移動量。
    delta_h: int 横方向の移動量。
    """
    mv = sv + delta_v
    mh = sh + delta_h
    while 0<=mv<=7 and 0<=mh<=7:
        if c_board.cross_board[mv][mh]==0:
            setlist.append([mv,mh])
        elif c_board.cross_board[mv][mh].iswhite!=ch_iswhite: #異色の駒の場合、takeできるが、そこまでしか移動できない
            setlist.append([mv,mh])
            break
        else:
            break
        mv += delta_v
        mh += delta_h
