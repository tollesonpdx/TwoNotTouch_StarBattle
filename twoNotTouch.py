import time
import copy
import random

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


class board(object):
    def __init__(self, size):
        self.size = size
        self.regionList = self.create_region_list()
        self.regions = self.create_regions()
        
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

    def create_region_list(self):
        rl = []
        remaining_squares = self.size * self.size
        assigned_squares = 0
        for i in range(0, self.size):
            if i < self.size - 1:
                reg_size = random.randrange(1, (remaining_squares - (self.size - i)))
            else:
                reg_size = remaining_squares
            rl.append([i, reg_size])
            remaining_squares -= reg_size
            assigned_squares += reg_size
        print('Remaining:', remaining_squares)
        print('Assigned:', assigned_squares)
        print('Regions List:', rl)
        return rl

    def create_regions(self):
        r = ['_'] * self.size * self.size
        for i, j in self.regionList:
            new_reg_bool = False
            while not new_reg_bool:
                new_reg = random.randrange(0,len(r))
                if (r[new_reg] == '_'):
                    r[new_reg] = i
                    new_reg_bool = True
        # add flood fill algo here  https://en.wikipedia.org/wiki/Flood_fill
        r = tuple(r)
        return r
    
    def print_board(self):
        print()
        grid = [[" _" for i in range(self.size)]]
        for i in range(self.size):
            list1 = []
            for j in range(self.size * 2 +1):
                if (j % 2) == 0: list1.append("|")
                else:
                    if i == j:
                        list1.append(bcolors.CRED + "*" + bcolors.ENDC)
                    else:
                        list1.append(bcolors.CVIOLET + "_" + bcolors.ENDC)
            grid.append(list1)
        for row in grid:
            print("".join(row))

    def print_board_2(self):
        print()
        for i in range(self.size):
            for j in range(self.size):
                if i == j:
                    print(bcolors.CRED2 + STAR + bcolors.ENDC, sep='', end='')
                else:
                    print(bcolors.CGREEN2 + EMPTY + bcolors.ENDC, sep='', end='')
            print()


if __name__ == "__main__":
    boardA = board(8)
    print('Regions:\n',boardA.regions)
    boardA.print_board()
    boardA.print_board_2()