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
