import sys
import pygame
from   pygame.locals import *
import global_value as glb
import ai_chess


glb.expected_piece_get = [
 {"pawn":142, "knight":784, "bishop":828, "rook":1286, "queen":2528, "king":10000000},
 {"pawn":207, "knight":868, "bishop":916, "rook":1378, "queen":2698, "king":10000000}]


glb.expected_tbl = [
    {"pawn":[[0,0,0,0,0,0,0,0],[-4,20,-8,-4,-4,-8,20,-4],[-6,-8,-6,-2,-2,-6,-8,-6],[-6,5,3,21,21,3,5,-6],[-17,-9,20,35,35,20,-9,-17],[-18,-2,19,24,24,19,-2,-18],[-11,6,7,3,3,7,6,-11],[0,0,0,0,0,0,0,0]],
     "knight":[[-195,-67,-42,-29,-29,-42,-67,-195],[-63,-19,5,14,14,5,-19,-63],[-11,37,56,65,65,56,37,-11],[-26,16,38,50,50,38,16,-26],[-25,18,43,47,47,43,18,-25],[-71,-22,0,9,9,0,-22,-71],[-83,-43,-21,-10,-10,-21,-43,-83],[-161,-96,-80,-73,-73,-80,-96,-161]],
     "bishop":[[-35,-11,-19-29,-29,-19,-11,-35],[-23,17,6,-2,-2,6,17,-23],[-17,16,12,2,2,12,16,-17],[-11,27,16,9,9,16,27,-11],[-11,28,21,10,10,21,28,-11],[-9,27,21,11,11,21,27,-9],[-20,20,12,1,1,12,20,-20],[-44,-13,-25-34,-34,-25,-13,-44]],
     "rook":[[-23,-15,-11,-5,-5,-11,-15,-23],[-12,4,8,12,12,8,4,-12],[-21,-7,0,2,2,0,-7,-21],[-22,-7,0,1,1,0,-7,-22],[-22,-6,-1,2,2,-1,-6,-22],[-21,-9,-4,2,2,-4,-9,-21],[-21,-8,-3,0,0,-3,-8,-21],[-25,-16,-16,-9,-9,-16,-16,-25]],
     "queen":[[-1,-4,-1,0,0,-1,-4,-1],[-2,7,7,6,6,7,7,-2],[-2,6,8,10,10,8,6,-2],[-3,9,8,7,7,8,9,-3],[-1,8,10,7,7,10,8,-1],[-2,6,9,9,9,9,6,-2],[-4,6,9,8,8,9,6,-4],[0,-4,-3,-1,-1,-3,-4,0]],
     "king":[[64,87,49,0,0,49,87,64],[87,120,64,25,25,64,120,87],[122,159,85,36,36,85,159,122],[145,176,112,69,69,112,176,145],[169,191,136,108,108,136,191,169],[198,253,168,120,120,168,253,198],[277,305,241,183,183,241,305,277],[272,325,273,190,190,273,325,272]]
    },
    {"pawn":[[0,0,0,0,0,0,0,0],[3,-9,1,18,18,1,-9,3],[8,-5,2,4,4,2,-5,8],[8,9,7,-6,-6,7,9,8],[3,3,-8,-3,-3,-8,3,3],[-4,-5,5,4,4,5,-5,-4],[7,-4,8,-2,-2,8,-4,7],[0,0,0,0,0,0,0,0]],
     "knight":[[-109,-89,-50,-13,-13,-50,-89,-109],[-65,-50,-24,13,13,-24,-50,-65],[-54,-38,-7,27,27,-7,-38,-54],[-46,-25,3,40,40,3,-25,-46],[-41,-25,6,38,38,6,-25,-41],[-50,-39,-7,28,28,-7,-39,-50],[-69,-54,-17,9,9,-17,-54,-69],[-105,-82,-46,-14,-14,-46,-82,-105]],
     "bishop":[[-55,-32,-36,-17,-17,-36,-32,-55],[-34,-10,-12,6,6,-12,-10,-34],[-24,-2,0,13,13,0,-2,-24],[-26,-4,-7,14,14,-7,-4,-26],[-26,-3,-5,16,16,-5,-3,-26],[-23,0,-3,16,16,-3,0,-23],[-34,-9,-14,4,4,-14,-9,-34],[-58,-31,-37,-19,-19,-37,-31,-58]],
     "rook":[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
     "queen":[[-74,-55,-43,-30,-30,-43,-55,-74],[-55,-30,-21,-6,-6,-21,-30,-55],[-40,-16,-10,3,3,-10,-16,-40],[-27,-5,10,21,21,10,-5,-27],[-29,-5,9,19,19,9,-5,-29],[-39,-17,-8,5,5,-8,-17,-39],[-56,-30,-21,-5,-5,-21,-30,-56],[-71,-56,-42,-29,-29,-42,-56,-71]],
     "king":[[5,60,75,75,75,75,60,5],[40,99,128,141,141,128,99,40],[87,164,174,189,189,174,164,87],[98,166,197,194,194,197,166,98],[103,152,168,169,169,168,152,103],[86,138,165,173,173,165,138,86],[57,98,138,131,131,138,98,57],[0,41,80,93,93,80,41,0]]
    }
]

