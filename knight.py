"""
ナイトの駒を定義したクラスファイル。
"""
from chess import *
from chess_piece import ChessPiece

class Knight(ChessPiece):
    """
    ナイトの駒クラス。
    """
    name = "knight"
    h_off = 232 - VS_HZURE
    v_off = 108
    vs_hoff = 917
    vs_voff = 108
    
    def __init__(self, h=0, v=0, iswhite=0):
        super().__init__(h, v, iswhite)

    def draw_piece(self, offx=0, offy=0):
        if glb.mx < 800:
            x = Knight.h_off + self.h * B_YOKO_OFF + offx
            y = Knight.v_off + self.v * B_TATE_OFF + offy
        else:
            x = Knight.h_off + self.h * B_YOKO_OFF - offx
            y = Knight.v_off + self.v * B_TATE_OFF - offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_knight[self.iswhite])

        if glb.mx < 800:
            x = Knight.vs_hoff + (7 - self.h) * B_YOKO_OFF - offx
            y = Knight.vs_voff + (7 - self.v) * B_TATE_OFF - offy
        else:
            x = Knight.vs_hoff + (7 - self.h) * B_YOKO_OFF + offx
            y = Knight.vs_voff + (7 - self.v) * B_TATE_OFF + offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_knight[self.iswhite])

    def is_moveable(self, h, v):
        if (h - self.h == 0) and (v - self.v == 0):  # 同じマスには移動できない（パスできない）
            return False

        canmove = []
        if self.v-2 >= 0:
            if self.h-1 >= 0:   #上左
                if c_board.cross_board[(self.v-2)][self.h-1]==0 or c_board.cross_board[(self.v-2)][self.h-1].iswhite != self.iswhite:
                    canmove.append([(self.v-2),self.h-1])
            if self.h+1 <= 7:   #上右
                if c_board.cross_board[(self.v-2)][self.h+1]==0 or c_board.cross_board[(self.v-2)][self.h+1].iswhite != self.iswhite:
                    canmove.append([(self.v-2),self.h+1])
        if self.v+2 <= 7:
            if self.h-1 >= 0:   # 下左
                if c_board.cross_board[(self.v+2)][self.h-1]==0 or c_board.cross_board[(self.v+2)][self.h-1].iswhite != self.iswhite:
                    canmove.append([(self.v+2),self.h-1])
            if self.h+1 <= 7:   # 下右
                if c_board.cross_board[(self.v+2)][self.h+1]==0 or c_board.cross_board[(self.v+2)][self.h+1].iswhite != self.iswhite:
                    canmove.append([(self.v+2),self.h+1])
        if self.h-2 >= 0:
            if self.v-1 >= 0:   # 左上
                if c_board.cross_board[(self.v-1)][self.h-2]==0 or c_board.cross_board[(self.v-1)][self.h-2].iswhite != self.iswhite:
                    canmove.append([(self.v-1),self.h-2])
            if self.v+1 <= 7:   # 左下
                if c_board.cross_board[(self.v+1)][self.h-2]==0 or c_board.cross_board[(self.v+1)][self.h-2].iswhite != self.iswhite:
                    canmove.append([(self.v+1),self.h-2])
        if self.h+2 <= 7:
            if self.v-1 >= 0:   # 右上
                if c_board.cross_board[(self.v-1)][self.h+2]==0 or c_board.cross_board[(self.v-1)][self.h+2].iswhite != self.iswhite:
                    canmove.append([(self.v-1),self.h+2])
            if self.v+1 <= 7:   # 右下
                if c_board.cross_board[(self.v+1)][self.h+2]==0 or c_board.cross_board[(self.v+1)][self.h+2].iswhite != self.iswhite:
                    canmove.append([(self.v+1),self.h+2])

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
        canmove.append([(self.v-2),self.h-1])
        canmove.append([(self.v-2),self.h+1])
        canmove.append([(self.v+2),self.h-1])
        canmove.append([(self.v+2),self.h+1])
        canmove.append([(self.v-1),self.h-2])
        canmove.append([(self.v+1),self.h-2])
        canmove.append([(self.v-1),self.h+2])
        canmove.append([(self.v+1),self.h+2])

        for mpos in canmove[:]: #範囲外のチェック
            if 0<=mpos[0]<=7 and 0<=mpos[1]<=7:
                expected_value = 0
                expected_value += glb.expected_tbl[glb.now_gamewave][self.name][mpos[0]][mpos[1]] #移動先の期待値

                if c_board.cross_board[mpos[0]][mpos[1]]!=0:
                    if c_board.cross_board[mpos[0]][mpos[1]].iswhite == self.iswhite:    #同じ色の駒だったら進めません
                        canmove.remove(mpos)
                        continue
                    else:
                        expected_value += glb.expected_piece_get[glb.now_gamewave][c_board.cross_board[mpos[0]][mpos[1]].name] #取った相手駒の期待値
                movelist.append([self,mpos[0],mpos[1],expected_value]) #4つめの要素に評価値を持たせます

        return movelist