
import copy

EMPTY = '\U000025A1'
STAR = '\U00002605'

class bcolors:
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'
    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class boardList:
    a = ((0,0,1,1,2,2,2,2),
         (3,3,3,1,1,2,2,2),
         (4,4,4,4,1,2,2,2),
         (4,4,4,4,4,4,2,2),
         (5,6,6,6,4,4,2,2),
         (5,6,6,6,6,6,6,6),
         (5,5,7,7,7,7,6,6),
         (7,7,7,7,7,7,7,7))
    b = ((0,0,0,0,0,0,0,0,1,1),
         (2,0,0,0,0,0,0,3,1,1),
         (2,2,2,2,3,3,3,3,1,1),
         (2,2,2,4,4,4,4,4,4,4),
         (2,2,5,5,5,4,4,4,4,6),
         (2,2,5,5,7,7,8,8,6,6),
         (9,9,5,5,7,8,8,8,6,6),
         (9,9,5,5,7,8,8,8,6,6),
         (9,9,5,5,7,8,8,8,6,6),
         (9,9,5,5,5,8,8,6,6,6))

class board(object):
    def __init__(self, option):
        self.regions = option
        self.size = len(self.regions[0])
        self.regionList = self.create_region_list()
        
    def create_region_list(self):
        rl =   [[0,[], bcolors.CWHITE],
                [1,[], bcolors.CRED2],
                [2,[], bcolors.CBLUE],
                [3,[], bcolors.CGREEN],
                [4,[], bcolors.CGREY],
                [5,[], bcolors.CRED],
                [6,[], bcolors.CVIOLET],
                [7,[], bcolors.CYELLOW],
                [8,[], bcolors.CBLACK],
                [9,[], bcolors.CGREEN2]]
        for i in range(self.size):
            row = self.regions[i]
            for j in range(self.size):
                item = row[j]
                rl[item][1].append((i,j))
        return tuple(rl)
    
    def print_board(self, stars):
        print()
        grid = []
        for i in range(self.size):
            row = []
            for j in range(self.size * 2 +1):
                if (j % 2) == 0: row.append(" ")
                else:
                    # if i == (j-1)/2:
                    if ( (i,((j-1)/2)) in stars ):
                        value = "*"
                    else:
                        value = "O"
                    color = self.regionList[self.regions[i][int((j-1)/2)]][2]
                    row.append(color + value + bcolors.ENDC)
            grid.append(row)
        for row in grid:
            print("".join(row))

    def print_board_2(self):
        print()
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    value = STAR
                else:
                    value = EMPTY
                color = self.regionList[self.regions[i][j]][2]
                print(color + value + bcolors.ENDC, sep='', end='')
            print()


if __name__ == "__main__":

    testStars = [(1,7),(6,4),(9,0)]
    
    if (0):
        boardA = board(boardList.a)
        print('Board, in Tuples:\n',boardA.regions)
        print('List of Regions:\n',boardA.regionList)
        boardA.print_board()
        boardA.print_board_2()

    boardB = board(boardList.b)
    if (0): 
        print('Board, in Tuples:\n',boardB.regions)
        print('List of Regions:\n',boardB.regionList)
        boardB.print_board_2()
    boardB.print_board(testStars)
