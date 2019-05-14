import json
import os
import sys
from .ColorDefine import Color

class ChessBoard:
    def __init__(self, V, H, WhoFirst):
        self.ChangeBoard(V, H, WhoFirst)

    def ChangeBoard(self, V, H, WhoFirst):
        self.V = V
        self.H = H
        self.WhoFirst = WhoFirst

    def NewGame(self):
        self.board = [Color.N] * (self.V * self.H)
        self.steps = []

    def Put(self, x, y):
        if self.board[x * self.V + y] != Color.N:
            return False
        else:
            color = Color.next(len(self.steps))
            self.board[x * self.V + y] = color
            self.steps.append([x, y, color])
            return True

    def IfWin(self):
        return False

    def Repent(self):
        if len(self.steps) == 0:
            return False
        else:
            x, y, color = self.steps.pop()
            self.board[x * self.V + y] = Color.N
            return True

    def Save(self, file):
        allInfo = {
            'V'         : self.V,
            'H'         : self.H,
            'WhoFirst'  : self.WhoFirst,
            'Steps'     : self.steps,
        }
        json.dump(allInfo, file)

        
    def Load(self, allInfo):
        for x, y, color in allInfo['Steps']:
            if not self.Put(x, y, color):
                self.NewGame()
                return False
        return True
