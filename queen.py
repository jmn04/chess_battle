"""
クイーンの駒を定義したクラスファイル。
"""
from chess import *
from chess_piece import ChessPiece

class Queen(ChessPiece):
    """
    クイーンの駒クラス。
    """
    name = "queen"
    h_off = 234 - VS_HZURE
    v_off = 97
    vs_hoff = 919
    vs_voff = 97
    
    def __init__(self, h=0, v=0, iswhite=0):
        super().__init__(h, v, iswhite)

    def draw_piece(self, offx=0, offy=0):
        if glb.mx < 800:
            x = Queen.h_off + self.h * B_YOKO_OFF + offx
            y = Queen.v_off + self.v * B_TATE_OFF + offy
        else:
            x = Queen.h_off + self.h * B_YOKO_OFF - offx
            y = Queen.v_off + self.v * B_TATE_OFF - offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_queen[self.iswhite])

        if glb.mx < 800:
            x = Queen.vs_hoff + (7 - self.h) * B_YOKO_OFF - offx
            y = Queen.vs_voff + (7 - self.v) * B_TATE_OFF - offy
        else:
            x = Queen.vs_hoff + (7 - self.h) * B_YOKO_OFF + offx
            y = Queen.vs_voff + (7 - self.v) * B_TATE_OFF + offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_queen[self.iswhite])

    def is_moveable(self, h, v):
        if (h - self.h == 0) and (v - self.v == 0):  # 同じマスには移動できない（パスできない）
            return False

        canmove = []
        passage_check(canmove, self.iswhite, self.v, self.h, -1, 0)
        passage_check(canmove, self.iswhite, self.v, self.h, 1, 0)
        passage_check(canmove, self.iswhite, self.v, self.h, 0, -1)
        passage_check(canmove, self.iswhite, self.v, self.h, 0, 1)
        passage_check(canmove, self.iswhite, self.v, self.h, -1, -1)
        passage_check(canmove, self.iswhite, self.v, self.h, 1, 1)
        passage_check(canmove, self.iswhite, self.v, self.h, 1, -1)
        passage_check(canmove, self.iswhite, self.v, self.h, -1, 1)

        for movedpos in canmove: #移動先があるかチェック
            if movedpos == [v,h]:
                return True
        else:
            return False
    
    def move(self, h, v):
        super().move(h, v)
        
    def next_move(self, iswhite=0, movelist=[]):
        super().next_move(iswhite, movelist)
        canmove = []
        passage_check(canmove, iswhite, self.v, self.h, -1,  0)
        passage_check(canmove, iswhite, self.v, self.h,  1,  0)
        passage_check(canmove, iswhite, self.v, self.h,  0, -1)
        passage_check(canmove, iswhite, self.v, self.h,  0,  1)
        passage_check(canmove, iswhite, self.v, self.h, -1, -1)
        passage_check(canmove, iswhite, self.v, self.h,  1,  1)
        passage_check(canmove, iswhite, self.v, self.h,  1, -1)
        passage_check(canmove, iswhite, self.v, self.h, -1,  1)

        for mpos in canmove[:]:
            expected_value = 0
            expected_value += glb.expected_tbl[glb.now_gamewave][self.name][mpos[0]][mpos[1]] #移動先の期待値
            if c_board.cross_board[mpos[0]][mpos[1]]!=0:
                expected_value += glb.expected_piece_get[glb.now_gamewave][c_board.cross_board[mpos[0]][mpos[1]].name] #取った相手駒の期待値

            movelist.append([self,mpos[0],mpos[1],expected_value]) #4つめの要素に評価値を持たせます

        return movelist
        