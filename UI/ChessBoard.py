import json
import os
import sys
from .ColorDefine import Color

class ChessBoard:
    def __init__(self, H, V, WhoFirst):
        self.ChangeBoard(V, H, WhoFirst)
        self.NewGame()

    def ChangeBoard(self, H, V, WhoFirst):
        self.H = H
        self.V = V
        self.WhoFirst = WhoFirst

    def NewGame(self):
        # self.board = [[Color.N for x in range(self.H)] for y in range(self.V)]
        self.board = [Color.N] * (self.H * self.V)
        self.steps = []

    def Put(self, x, y):
        if self.board[y * self.H + x] != Color.N:
            return False
        else:
            color = Color.next(len(self.steps))
            self.board[y * self.H + x] = color
            self.steps.append([x, y])
            return True

    def IfWin(self):
        return False

    def Repent(self):
        if len(self.steps) == 0:
            return False
        else:
            x, y = self.steps.pop()
            color = Color.next(len(self.steps))
            self.board[y * self.H + x] = Color.N
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
        for x, y in allInfo['Steps']:
            if self.CheckFull():
                raise Exception('error of Full')
            elif not self.Put(x, y):
                self.NewGame()
                raise Exception('error in Put into Board')
            elif self.CheckWin():
                raise Exception('error of Sucess')

    def CheckFull(self):
        return len(self.steps) == self.H * self.V

    def CheckWin(self):
        X, Y = self.steps[-1]
        color = Color.next(len(self.steps) - 1)

        def nextN(x, y):
            return x, y + 1
        def nextS(x, y):
            return x, y - 1
        def nextE(x, y):
            return x + 1, y
        def nextW(x, y):
            return x - 1, y

        def nextNE(x, y):
            return x + 1, y + 1
        def nextSE(x, y):
            return x + 1, y - 1
        def nextNW(x, y):
            return x - 1, y + 1
        def nextSW(x, y):
            return x - 1, y - 1

        def isLegal(x, y):
            return x >=0 and x < self.H and y >=0 and y < self.V

        def destNum(nextFunc):
            x, y = X, Y
            for n in range(5):
                x, y = nextFunc(x, y)
                if not isLegal(x, y) or self.board[y * self.H + x] != color:
                    return n
            return 5

        if  destNum(nextN) + destNum(nextS) >= 5 or\
            destNum(nextE) + destNum(nextW) >= 5 or\
            destNum(nextNE) + destNum(nextSW) >= 5 or\
            destNum(nextSE) + destNum(nextNW) >= 5:
            return True
        else:
            return False
