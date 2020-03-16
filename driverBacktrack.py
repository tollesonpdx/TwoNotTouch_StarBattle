# --------------------------------------------------------------
#                             main
# --------------------------------------------------------------
import backTrack as bt
from collections import namedtuple


duck = bt.Duck(bill='wide orange', tail='long')
print(duck.bill)

#board = ((0,0,1,1,2,2,2,2),
#         (3,3,3,1,1,2,2,2),
#         (4,4,4,4,1,2,2,2),
#         (4,4,4,4,4,4,2,2),
#         (5,6,6,6,4,4,2,2),
#         (5,6,6,6,6,6,6,6),
#         (5,5,7,7,7,7,6,6),
#         (7,7,7,7,7,7,7,7))

board = ((1, 2, 2, 2, 2, 2, 2, 2, 2),
        (1, 2, 2, 2, 2, 4, 4, 4, 2),
        (1, 3, 3, 3, 3, 4, 4, 4, 2),
        (1, 3, 5, 3, 5, 4, 6, 4, 9),
        (1, 3, 5, 5, 5, 4, 6, 4, 9),
        (1, 3, 5, 7, 5, 9, 6, 9, 9),
        (1, 1, 1, 7, 7, 9, 9, 9, 8),
        (1, 1, 7, 7, 8, 8, 8, 8, 8),
        (1, 1, 1, 7, 8, 8, 8, 8, 8))

maxRow = len(board)
maxCol = len(board[0])

regionDomains = bt.region_domains(board)

# set of variables- each variable is one of two stars in region
X = bt.init_variables(regionDomains.keys())

#assignments where key is var from X
assignments= bt.init_assignments(X)

# dictionary of  var: domain, set of coord 
D = bt.init_domains(X, regionDomains)

#constraint = ()
C=bt.notTooClose

# use named tuple for CSP
Duck = namedtuple('Duck', 'bill tail')
duck =Duck(bill='wide orange', tail='long')
#print(duck.bill)

CSP = namedtuple('CSP', 'X D C')
csp = CSP(X=X, D=D, C=C)



Assignment = namedtuple('Assignment', 'vals unavailable')
assignment = Assignment({'1A':1, '1B':2}, {1,2})

solution = bt.backtracking_search(csp)
print(solution.vals.values())


# constraints
# star from same region have different locations- costar(var)
# no two touch from any region-  neighbors(coord)
# only two othe star in same row / col from any region row(coord), col(cood)