# --------------------------------------------------------------
#                             main
# --------------------------------------------------------------
import backTrack as bt
from collections import namedtuple


duck = bt.Duck(bill='wide orange', tail='long')
print(duck.bill)

board = ((0,0,1,1,2,2,2,2),
         (3,3,3,1,1,2,2,2),
         (4,4,4,4,1,2,2,2),
         (4,4,4,4,4,4,2,2),
         (5,6,6,6,4,4,2,2),
         (5,6,6,6,6,6,6,6),
         (5,5,7,7,7,7,6,6),
         (7,7,7,7,7,7,7,7))

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

bt.backtracking_search(csp)

# constraints
# star from same region have different locations- costar(var)
# no two touch from any region-  neighbors(coord)
# only two othe star in same row / col from any region row(coord), col(cood)