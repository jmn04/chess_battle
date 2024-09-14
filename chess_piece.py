"""
チェスの駒を定義したスーパークラスファイル。
"""

from chess import c_board
from abc import ABCMeta, abstractmethod
import global_value as glb

class ChessPiece(metaclass=ABCMeta):
    """
    チェスの駒の抽象クラス。
    各駒クラスはこのクラスを継承して作成する。
    """
    def __init__(self, h=0, v=0, iswhite=0): # h=0～7, v=0～7, iswhite=0:black,1:white
        self.h = h
        self.v = v
        self.iswhite = iswhite
        self.pick = False   # 自分がマウスでつかまれているか
        c_board.cross_board[v][h] = self

    @abstractmethod # 抽象メソッド
    def draw_piece(self, offx=0, offy=0):
        """
        駒を描画するメソッド。
        """
        pass

    @abstractmethod # 抽象メソッド
    def is_moveable(self, h: int, v: int): # h=0～7, v=0～7 右上マスを(0,0)とする
        """
        移動可能かどうかを判定するメソッド。
        
        --- Parameters ---\n
        h: int 0~7 横方向の移動先。
        v: int 0~7 縦方向の移動先。
        
        --- Returns ---\n
        bool: 移動可能ならTrue、不可能ならFalseを返す。
        """
        pass

    def move(self, h: int, v: int):
        """
        駒を移動させるメソッド。
        
        --- Parameters ---\n
        h: int 0~7 横方向の移動先。
        v: int 0~7 縦方向の移動先。
        """
        c_board.cross_board[self.v][self.h] = 0
        self.h = h
        self.v = v
        c_board.cross_board[v][h] = self
    
    @abstractmethod # 抽象メソッド
    def next_move(self, iswhite=0, movelist=[]):
        """
        次の手を計算するメソッド。
        
        --- Parameters ---\n
        iswhite: int 0~1 白か黒かを表す。
        movelist: list 次の移動先のリスト。
        movedeltas: 移動方向とステップ数を表すリスト
        """
        if iswhite != self.iswhite:
            return
        