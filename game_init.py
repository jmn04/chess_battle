"""
ゲームのグローバル設定を初期化するメソッドを定義したファイル。
"""
import os
from chess import *
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from pawn import Pawn

def init():
    """
    ゲームのグローバル設定を初期化するメソッド。
    """
    glb.downflg = False
    glb.mx = 0
    glb.my = 0

    #画像ファイルの読み込み
    os.chdir("./images") #画像ファイルのあるディレクトリに移動
    glb.img_board_base = pygame.image.load("ボードnew.jpg")  #幅1202 高さ1202
    glb.img_piece_base = pygame.image.load("ピース.png")  #幅3478 高さ2446
    #画像のサイズ調整
    glb.img_board = pygame.transform.scale(glb.img_board_base, (800, 800))
    glb.img_piece = pygame.transform.scale(glb.img_piece_base, (193,136))

    glb.front_white = True  #手前を先手=True, 後手=False
    glb.c_board_inst = c_board()    #ゲーム版のインスタンス

    #初期盤面の作成
    if glb.front_white: #手前が先手（白）
        glb.w_piece = [King(4,0,0),Queen(3,0,0),Bishop(5,0,0),Bishop(2,0,0),Knight(6,0,0),Knight(1,0,0),Rook(7,0,0),Rook(0,0,0),
                       Pawn(0,1,0),Pawn(1,1,0),Pawn(2,1,0),Pawn(3,1,0),Pawn(4,1,0),Pawn(5,1,0),Pawn(6,1,0),Pawn(7,1,0)]
        glb.b_piece = [King(4,7,1),Queen(3,7,1),Bishop(5,7,1),Bishop(2,7,1),Knight(6,7,1),Knight(1,7,1),Rook(7,7,1),Rook(0,7,1),
                       Pawn(0,6,1),Pawn(1,6,1),Pawn(2,6,1),Pawn(3,6,1),Pawn(4,6,1),Pawn(5,6,1),Pawn(6,6,1),Pawn(7,6,1)]
    else:
        glb.w_piece = [King(3,0,1),Queen(4,0,1),Bishop(5,0,1),Bishop(2,0,1),Knight(6,0,1),Knight(1,0,1),Rook(7,0,1),Rook(0,0,1),
                       Pawn(0,1,1),Pawn(1,1,1),Pawn(2,1,1),Pawn(3,1,1),Pawn(4,1,1),Pawn(5,1,1),Pawn(6,1,1),Pawn(7,1,1)]
        glb.b_piece = [King(3,7,0),Queen(4,7,0),Bishop(5,7,0),Bishop(2,7,0),Knight(6,7,0),Knight(1,7,0),Rook(7,7,0),Rook(0,7,0),
                       Pawn(0,6,0),Pawn(1,6,0),Pawn(2,6,0),Pawn(3,6,0),Pawn(4,6,0),Pawn(5,6,0),Pawn(6,6,0),Pawn(7,6,0)]
        