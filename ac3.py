class ac_csp():
    def __init__(self, board):
        self.board = board
        self.vars = self.get_vars(board)
        self.arcs = self.make_arcs()
        self.domain = self.create_domain
        self.constraints = self.create_constraints

    def get_vars(self, board):
        vars = []
        rowcount = 0
        for row in board:
            colcount = 0
            for col in row:
                coords = [colcount, rowcount]
                vars.append(coords)
                colcount += 1
                print("Colcount = ", colcount)
            rowcount += 1
        return vars

    def make_arcs(self):
        arcs = []
        coords = self.vars
        for i in coords:
            # print("The value of i is", i)
            c1 = i
            for j in coords:
                    arc = []
                    c2 = j

                    '''
                    We can pre-emptively constrain the list of arcs from containing duplicate coordinates for i and j
                    since two stars can't be in the same square.  This will eliminate n total results from the arcs,
                    so we should end up with (n ** 2) - n arcs.
                    '''

                    if not c1 == c2:
                        arc.append(c1)
                        arc.append(c2)
                        if arc not in arcs:
                            arcs.append(arc)
        return arcs

    def create_domain(self):
        print("TODO")

    def create_constraints(self):
        print("TODO")
