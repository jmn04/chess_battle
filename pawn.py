"""
ポーンの駒を定義したクラスファイル。
"""
from chess import *
from chess_piece import ChessPiece

class Pawn(ChessPiece):
    """
    ポーンの駒クラス。
    """
    name = "pawn"
    h_off = 235 - VS_HZURE
    v_off = 123
    vs_hoff = 920
    vs_voff = 123
    
    def __init__(self, h=0, v=0, iswhite=0):
        super().__init__(h, v, iswhite)

    def draw_piece(self, offx=0, offy=0):
        if glb.mx < 800:
            x = Pawn.h_off + self.h * B_YOKO_OFF + offx
            y = Pawn.v_off + self.v * B_TATE_OFF + offy
        else:
            x = Pawn.h_off + self.h * B_YOKO_OFF - offx
            y = Pawn.v_off + self.v * B_TATE_OFF - offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_pawn[self.iswhite])

        if glb.mx < 800:
            x = Pawn.vs_hoff + (7 - self.h) * B_YOKO_OFF - offx
            y = Pawn.vs_voff + (7 - self.v) * B_TATE_OFF - offy
        else:
            x = Pawn.vs_hoff + (7 - self.h) * B_YOKO_OFF + offx
            y = Pawn.vs_voff + (7 - self.v) * B_TATE_OFF + offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_pawn[self.iswhite])

    def is_moveable(self, h, v):
        canmove = []
        if self.iswhite:  # 白
            if self.v == 6 and v == 4 and h == self.h and c_board.cross_board[5][self.h] == 0 and c_board.cross_board[4][self.h] == 0:
                canmove.append([4, self.h])
            if self.v - 1 >= 0:
                if c_board.cross_board[self.v - 1][self.h] == 0 and v == self.v - 1 and h == self.h:
                    canmove.append([self.v - 1, self.h])
                if h == self.h - 1 and v == self.v - 1 and c_board.cross_board[self.v - 1][self.h - 1] != 0 and c_board.cross_board[self.v - 1][self.h - 1].iswhite != self.iswhite:
                    canmove.append([self.v - 1, self.h - 1])
                if h == self.h + 1 and v == self.v - 1 and c_board.cross_board[self.v - 1][self.h + 1] != 0 and c_board.cross_board[self.v - 1][self.h + 1].iswhite != self.iswhite:
                    canmove.append([self.v - 1, self.h + 1])
        else:  # 黒
            if self.v == 1 and v == 3 and h == self.h and c_board.cross_board[2][self.h] == 0 and c_board.cross_board[3][self.h] == 0:
                canmove.append([3, self.h])
            if self.v + 1 <= 7:
                if c_board.cross_board[self.v + 1][self.h] == 0 and v == self.v + 1 and h == self.h:
                    canmove.append([self.v + 1, self.h])
                if h == self.h - 1 and v == self.v + 1 and c_board.cross_board[self.v + 1][self.h - 1] != 0 and c_board.cross_board[self.v + 1][self.h - 1].iswhite != self.iswhite:
                    canmove.append([self.v + 1, self.h - 1])
                if h == self.h + 1 and v == self.v + 1 and c_board.cross_board[self.v + 1][self.h + 1] != 0 and c_board.cross_board[self.v + 1][self.h + 1].iswhite != self.iswhite:
                    canmove.append([self.v + 1, self.h + 1])

        if (h - self.h == 0) and (v - self.v == 0):  # 同じマスには移動できない（パスできない）
                return False
        else:
            for poslist in canmove:
                if poslist == [v,h]:
                    return True
            else:
                return False
    
    def move(self, h, v):
        super().move(h, v)
    
    def next_move(self, iswhite=0, movelist=[]):
        super().next_move(iswhite, movelist)
        canmove = []

        #白・黒兼用（CPUは先手の場合も白が奥）
        if (self.v+1<=7) and c_board.cross_board[(self.v+1)][self.h]==0:    #1マス前進
            canmove.append([(self.v+1),self.h])
            if self.v==1 and c_board.cross_board[3][self.h]==0:   #最初の第一歩
                canmove.append([3,self.h])
        if (self.v+1<=7) and (self.h-1>=0) and c_board.cross_board[(self.v+1)][self.h-1]!=0 and (c_board.cross_board[(self.v+1)][self.h-1].iswhite!=self.iswhite):   #斜め1マスtake
                canmove.append([(self.v+1),self.h-1])
        if (self.v+1<=7) and (self.h+1<=7) and c_board.cross_board[(self.v+1)][self.h+1]!=0 and (c_board.cross_board[(self.v+1)][self.h+1].iswhite!=self.iswhite):   #斜め1マスtake
                canmove.append([(self.v+1),self.h+1])

        for mpos in canmove[:]:
            expected_value = 0
            expected_value += glb.expected_tbl[glb.now_gamewave][self.name][mpos[0]][mpos[1]] #移動先の期待値
            if c_board.cross_board[mpos[0]][mpos[1]]!=0:
                expected_value += glb.expected_piece_get[glb.now_gamewave][c_board.cross_board[mpos[0]][mpos[1]].name] #取った相手駒の期待値

            movelist.append([self,mpos[0],mpos[1],expected_value]) #4つめの要素に評価値を持たせます

        return movelist