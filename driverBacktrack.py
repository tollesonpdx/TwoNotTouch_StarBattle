import backTrack as bt
from collections import namedtuple

board = ((1, 2, 2, 2, 2, 2, 2, 2, 2),
        (1, 2, 2, 2, 2, 4, 4, 4, 2),
        (1, 3, 3, 3, 3, 4, 4, 4, 2),
        (1, 3, 5, 3, 5, 4, 6, 4, 9),
        (1, 3, 5, 5, 5, 4, 6, 4, 9),
        (1, 3, 5, 7, 5, 9, 6, 9, 9),
        (1, 1, 1, 7, 7, 9, 9, 9, 8),
        (1, 1, 7, 7, 8, 8, 8, 8, 8),
        (1, 1, 1, 7, 8, 8, 8, 8, 8))



csp = bt.CSP(board)
solution= csp.backtracking_search()
print(solution.vals.values())

medium = ((1,1,1,2,2,3,3,3,3),
(1,1,1,1,2,3,3,3,3),
(1,4,4,1,2,3,5,5,3),
(1,1,4,1,2,3,3,5,3),
(1,4,4,6,2,6,5,5,3),
(1,4,6,6,6,6,6,5,3),
(1,4,4,7,7,7,5,5,3),
(8,8,8,7,7,7,9,9,9),
(8,8,8,7,7,7,9,9,9))

cspMed = bt.CSP(medium)
solutionMed= cspMed.backtracking_search()
print(solutionMed.vals.values())

extraHard= ((1,1,2,2,2,2,3,3,3,3),
       (1,1,4,4,2,2,3,5,5,3),
       (1,4,4,6,6,2,5,5,5,5),
       (1,4,4,6,6,6,6,5,5,5),
       (1,4,4,4,7,7,7,5,5,5),
       (1,1,4,7,7,7,7,5,5,8),
       (9,9,9,7,7,7,7,7,8,8),
       (9,9,9,10,7,7,7,10,8,8),
       (9,9,9,10,10,7,10,10,8,8),
       (9,9,9,10,10,10,10,10,8,8))

cspEH = bt.CSP(extraHard)
solutionEH = cspEH.backtracking_search()
print(solutionEH.vals.values())


