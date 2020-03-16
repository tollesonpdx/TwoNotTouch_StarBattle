from itertools import permutations, chain, islice

class csp():
    def __init__(self, board, D=0, C=0):
        self.board = board
        self.vars = self.get_vars(board)
        self.arcs = self.make_arcs()
        self.domain = D
        self.constraints = C

    def get_vars(self, board):
        vars = []
        rowcount = 0
        for row in board:
            for col in row:
                colcount = 0
                coords = [colcount, rowcount]
                vars.append(coords)
                colcount += 1
            rowcount += 1
        return vars

    def make_arcs(self):
        arcs = []
        coords = self.vars
        for i in coords:
            # print("The value of i is", i)
            c1 = i
            for i in coords:
                if not c1 == i:
                    arc = []
                    c2 = i
                    arc.append(c1)
                    arc.append(c2)
                    if arc not in arcs:
                        arcs.append(arc)
        print(arcs)
        print(len(arcs))
        return arcs

    def create_domain(self):
        print("TODO")

    def create_constraints(self):
        print("TODO")
