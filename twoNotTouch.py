import time
import copy
import random

EMPTY = '\U000025A1'
STAR = '\U00002605'

class board(object):
    def __init__(self, size):
        self.size = size
        self.regionList = self.createRegionList()
        self.regions = self.createRegions()
        
        # # hard coded regions for testing
        # self.regions = (0,0,1,1,2,2,2,2,
        #                 3,3,3,1,1,2,2,2,
        #                 4,4,4,4,1,2,2,2,
        #                 4,4,4,4,4,4,2,2,
        #                 5,6,6,6,4,4,2,2,
        #                 5,6,6,6,6,6,6,6,
        #                 5,5,7,7,7,7,6,6,
        #                 7,7,7,7,7,7,7,7)
        # # hard coded for testing

    def createRegionList(self):
        rl = []
        remainingSquares = self.size * self.size
        assignedSquares = 0
        for i in range(0,self.size):
            if (i < self.size - 1):
                regSize = random.randrange(1,(remainingSquares - (self.size - i)))
            else:
                regSize = remainingSquares
            rl.append([i,regSize])
            remainingSquares -= regSize
            assignedSquares += regSize
        print('Remaining:',remainingSquares)
        print('Assigned:',assignedSquares)
        print('Regions List:',rl)
        return rl

    def createRegions(self):
        r = ['_'] * self.size * self.size
        for i,j in self.regionList:
            newRegBool = False
            while (newRegBool == False):
                newReg = random.randrange(0,len(r))
                if (r[newReg] == '_'):
                    r[newReg] = i
                    newRegBool = True
        # add flood fill algo here  https://en.wikipedia.org/wiki/Flood_fill
        r = tuple(r)
        return r
    
    def printBoard(self):
        print()
        grid = [[" _" for i in range(self.size)]]
        for i in range(self.size):
            list1 = []
            for j in range(self.size * 2 +1):
                if (j % 2) == 0: list1.append("|")
                else:
                    if (i == j):
                        list1.append("*")
                    else:
                        list1.append("_")
            grid.append(list1)
        for row in grid:
            print("".join(row))
    def printBoard_2(self):
        print()
        for i in range(self.size):
            for j in range(self.size):
                if (i == j):
                    print(STAR,sep='',end='')
                else:
                    print(EMPTY,sep='',end='')
            print()

if __name__ == "__main__":
    boardA = board(8)
    print ('Regions:\n',boardA.regions)
    boardA.printBoard()
    boardA.printBoard_2()