"""
キングの駒を定義したクラスファイル。
"""
from chess import *
from chess_piece import ChessPiece

class King(ChessPiece):
    """
    キングの駒クラス。
    """
    name = "king"
    alive = True # 生存フラグ（Falseでゲーム終了）
    h_off = 230 - VS_HZURE
    v_off = 80
    vs_hoff = 915
    vs_voff = 80
    
    def __init__(self, h=0, v=0, iswhite=0):
        super().__init__(h, v, iswhite)

    def draw_piece(self, offx=0, offy=0):
        if glb.mx < 800:
            x = King.h_off + self.h * B_YOKO_OFF + offx
            y = King.v_off + self.v * B_TATE_OFF + offy
        else:
            x = King.h_off + self.h * B_YOKO_OFF - offx
            y = King.v_off + self.v * B_TATE_OFF - offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_king[self.iswhite])

        if glb.mx < 800:
            x = King.vs_hoff + (7 - self.h) * B_YOKO_OFF - offx
            y = King.vs_voff + (7 - self.v) * B_TATE_OFF - offy
        else:
            x = King.vs_hoff + (7 - self.h) * B_YOKO_OFF + offx
            y = King.vs_voff + (7 - self.v) * B_TATE_OFF + offy
        glb.screen.blit(glb.img_piece, (x, y), area=rect_king[self.iswhite])

    def is_moveable(self, h, v):
        if (h - self.h == 0) and (v - self.v == 0):  # 同じマスには移動できない（パスできない）
            return False

        canmove = []
        canmove.append([(self.v-1),self.h])
        canmove.append([(self.v-1),self.h-1])
        canmove.append([(self.v-1),self.h+1])
        canmove.append([(self.v+1),self.h])
        canmove.append([(self.v+1),self.h-1])
        canmove.append([(self.v+1),self.h+1])
        canmove.append([(self.v),self.h-1])
        canmove.append([(self.v),self.h+1])

        for movedpos in canmove[:]:  # 範囲外のチェック
            if not (0 <= movedpos[0] <= 7 and 0 <= movedpos[1] <= 7):
                canmove.remove(movedpos)
                continue
            if c_board.cross_board[movedpos[0]][movedpos[1]] != 0:
                if c_board.cross_board[movedpos[0]][movedpos[1]].iswhite == self.iswhite:  # 同じ色の駒だったら進めない
                    canmove.remove(movedpos)
                    continue

        for movedpos in canmove: #移動先があるかチェック
            if movedpos == [v,h]:
                return True
        else:
            return False
        
    def next_move(self, iswhite=0, movelist=[]):
        super().next_move(iswhite, movelist)
        canmove = []
        canmove.append([(self.v-1), self.h,   0])
        canmove.append([(self.v-1), self.h-1, 0])
        canmove.append([(self.v-1), self.h+1, 0])
        canmove.append([(self.v+1), self.h,   0])
        canmove.append([(self.v+1), self.h-1, 0])
        canmove.append([(self.v+1), self.h+1, 0])
        canmove.append([(self.v),   self.h-1, 0])
        canmove.append([(self.v),   self.h+1, 0])

        for mpos in canmove[:]: #範囲外のチェック
            if not( 0<=mpos[0]<=7 and 0<=mpos[1]<=7 ):
                canmove.remove(mpos)
                continue
            mpos[2] += glb.expected_tbl[glb.now_gamewave][self.name][mpos[0]][mpos[1]] #移動先の期待値
            if c_board.cross_board[mpos[0]][mpos[1]]!=0:
                if c_board.cross_board[mpos[0]][mpos[1]].iswhite == self.iswhite:    #同じ色の駒だったら進めません
                    canmove.remove(mpos)
                    continue
                else:   #相手の駒を取れるので、期待値計算します
                    mpos[2] += glb.expected_piece_get[glb.now_gamewave][c_board.cross_board[mpos[0]][mpos[1]].name] #取った相手駒の期待値

        for mpos in canmove: #移動先を調査リストに追加
            #移動後の座標の評価値を加えます
            movelist.append([self,mpos[0],mpos[1],mpos[2]]) #4つめの要素に評価値を持たせます
        return movelist