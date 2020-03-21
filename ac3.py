import queue

'''
We can come up with a way to not hard code this - it's really only used in a couple of places
'''
NUM_STARS = 2

class ac_csp():
    def __init__(self, board):
        '''
        Initializes a Constraint Satisfaction Problem Class specific to the AC-3 algorithm
        :param board:
        '''
        self.board = board
        self.vars = self.get_vars(board)
        self.domain = self.create_domain(board)
        self.arcs = self.make_arcs()
        self.constraints = self.check_function(x=(0, 0), y=(0, 0)) # hard coded to make it run, currently
        self.solver_queue = queue.Queue()

    def get_vars(self, board):
        '''
        Takes in a board object and the NUM_STARS global (hard coded at 2 for now) and initializes n
        empty variables, where n is the length of one dimension of the board multiplied by the value of
        NUM_STARS (len(board) * NUM_STARS); the variables in the problem are the stars and their locations,
        so this will determine how many stars we need to place overall.
        :param board:
        :return:
        '''
        num_vars = (len(board) * NUM_STARS)
        vars = []
        for var in range(0, num_vars):
            vars.append([-1, -1])
        return vars

    def create_domain(self, board):
        '''
        Takes in a board object (from twoNotTouch.py) and creates a viable domain of (x,y) coordinates from that board
        :param board:
        :return:
        '''
        domain = []
        rowcount = 0
        for row in board:
            colcount = 0
            for i in range(len(row)):
                coords = [colcount, rowcount]
                domain.append(coords)
                colcount += 1
            rowcount += 1
        return domain

    def make_arcs(self):
        '''
        Takes in self.domain and makes (nearly) all the permutations of the possible coordinates, to serve as arcs for
        the queue. After it does this, it eliminates n-squared arcs (where n is cardinality or arity of the board) and
        arc coordinates i are equal to arc coordinates j; this removes any instances of a coordinate being repeated
        from the possible arc comparisons.
        :return: a list (of lists of lists) of arcs.
        '''
        arcs = []
        coords = self.domain
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

    def row_check(self, var1=(0, 0), var2=(0, 0)):
        '''
        Takes in our list of variables and checks whether any n are in the same row, where n is NUM_STARS.
        :param var1:
        :param var2:
        :return:
        '''
        rc_result = False
        rowcount = 0
        if not var1[0] == -1 and not var1[1] == -1:
            v1x = var1[0]
            v2x = var2[0]
            if v1x == v2x:
                rowcount += 1
                if rowcount >= NUM_STARS:
                    rc_result = True

        return rc_result

    def col_check(self, var1=(0, 0), var2=(0, 0)):
        '''
        Takes in our list of variables and checks whether any n have the same col, where n is NUM_STARS.
        :param vars: Looks in vars
        :return:
        '''
        cc_result = False
        colcount = 0
        v1y = var1[1]
        v2y = var2[1]
        if v1y == v2y:
            colcount += 1
            if colcount >= NUM_STARS:
                cc_result = True
        return cc_result

    def adjacency_check(self, var1=(0, 0), var2=(0, 0)):
        '''
        Checks for adjacency in a pair of coordinates (an arc) from the arcs queue, or of two variables passed in.
        :param var1: First coordinate from the arc
        :param var2: Second coordinate from the arc
        :return: Return False if there's no adjacency, True if there is an adjacency
        '''
        ac_result = False
        n1 = (var1[0]+1, var1[1]-1)
        n2 = (var1[0]+1, var1[1])
        n3 = (var1[0]+1, var1[1]+1)
        n4 = (var1[0], var1[1]-1)
        n5 = (var1[0], var1[1]+1)
        n7 = (var1[0]-1, var1[1]+1)
        n8 = (var1[0]-1, var1[1])
        n9 = (var1[0]-1, var1[1]+1)
        if n1 == var2 or n2 == var2 or n3 == var2 or n4 == var2 or n5 == var2 or n7 == var2 or n8 == var2 or n9 == var2:
            ac_result = True
        return ac_result

    def region_check(self, board):
        '''
        Looks at the values in the board and
        :param board:
        :return:
        '''
        return False

    def unique_check(self):
        '''
        This function has been deprecated but has been left in the code just in case - this check is no longer
        being used because we're removing the possibility of arcs of (x1, y1), (x1, y1) from the list of arcs.

        Makes a set out of the vars list, and checks whether the length of the set is equal to the number of stars
        we're attempting to put on the board; ignores the result if any of the stars have yet to be allocated.
        :param vars:
        :return:
        '''
        checkset = set(vars)
        not_all_allocated = True
        unique_result = True
        for var in self.vars:
            if type(var) != list:
                return not_all_allocated
        if not len(checkset) == (len(vars) * NUM_STARS):
            unique_result = False
        return unique_result

    def solve(self):
        result = self.solution_assistant
        return_value = []
        for step in result:
            '''
            If we can't take a step, we've found an inconsistency.
            '''
            if step == None:
                return step
            else:
                return_value = step

        '''
        We return only the final domain from the solver.
        '''
        return return_value[1]

    def check_function(self, x, y):
        '''
        Runs all the
        :param x: The first set of arc coordinates
        :param y: The second set of arc coordinates
        :return:
        '''
        rc = self.row_check(x, y)
        cc = self.col_check(x, y)
        adj = self.adjacency_check(x, y)
        reg = self.region_check(self.board)

        if rc == False or cc == False or adj == False or reg == False:
            constraints = False
        return constraints


    def solution_assistant(self):
        '''
        Programmer's note:

        Returns a generator for every step in the algorithm - including the end result
        Each of the yields is a tuple containing the edge, new domains, and other edges to consider.
        This function was initially coded against a much simpler AC3 implementation problem, but
        once the scope of domains, arcs and constraints was expanded to fit the formulation of the
        problem and all the issues inherent in getting AC3 to function on this problem were
        discovered, the project progressed beyond this implementation.  As a result of these many
        iterations, the AC3 algorithm no longer works or runs to completion.
        '''
        [self.solver_queue.put(arc) for arc in self.arcs]
        while not self.solver_queue.empty():
            (xi, xj) = self.solver_queue.get()

            if self.revise(xi, xj):
                if len(self.domain[xi]) == 0:
                    yield None
                    break

                neighbors = [neighbor for neighbor in self.arcs if neighbor[0] == xj]
                [self.solver_queue.put(neighbor) for neighbor in neighbors]

                yield ((xi, xj), self.domain, neighbors)
            else:
                yield ((xi, xj), self.domain, None)

    def revise(self, xi, xj):
        '''
        This function needs to be entirely recoded to work with the most recent formulation of the problem -
        unfortunately due to the issues that the most recent formulation of the problem still had with
        picking initial domain constraints for any of its variables.
        :return:
        '''
        revised = False
        xi_domain = self.domain[xi]
        xj_domain = self.domain[xj]

        # this part specifically won't work with the current problem formulation.
        constraints = [constraint for constraint in self.constraints if constraint[0] == xi and constraint[1] == xj]

        for x in xi_domain[:]:
            constraint_satisfaction = False
            for y in xj_domain[:]:
                for constraint in constraints:
                    check_function = self.constraints[constraint]
                    #check y against x for each constraint
                    if check_function(x, y):
                        constraint_satisfaction = True

            if not constraint_satisfaction:
                xi_domain.remove(x)
                revised = True

        return revised

