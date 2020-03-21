import backTrack as bt
from collections import namedtuple
import tnt_board as tb

easy1 = ((1, 2, 2, 2, 2, 2, 2, 2, 2),
        (1, 2, 2, 2, 2, 4, 4, 4, 2),
        (1, 3, 3, 3, 3, 4, 4, 4, 2),
        (1, 3, 5, 3, 5, 4, 6, 4, 9),
        (1, 3, 5, 5, 5, 4, 6, 4, 9),
        (1, 3, 5, 7, 5, 9, 6, 9, 9),
        (1, 1, 1, 7, 7, 9, 9, 9, 8),
        (1, 1, 7, 7, 8, 8, 8, 8, 8),
        (1, 1, 1, 7, 8, 8, 8, 8, 8))

easyBoardObj = tb.board(easy1)

csp = bt.CSP(easy1)
solution= csp.backtracking_search()
#print(solution.vals.values())
print('Easy 1')
easyBoardObj.print_board(solution.vals.values())
solution=None


easy2 = ((1,1,1,2,2,3,3,3,3),
(1,1,1,1,2,3,3,3,3),
(1,4,4,1,2,3,5,5,3),
(1,1,4,1,2,3,3,5,3),
(1,4,4,6,2,6,5,5,3),
(1,4,6,6,6,6,6,5,3),
(1,4,4,7,7,7,5,5,3),
(8,8,8,7,7,7,9,9,9),
(8,8,8,7,7,7,9,9,9))
easy2BoardObj = tb.board(easy2)
cspEasy2 = bt.CSP(easy2)
solution= cspEasy2.backtracking_search()
print('Easy 2')
easy2BoardObj.print_board(solution.vals.values())
solution=None

easy3= ((1,1,1,1,1,1,1,2,2,3),
(1,4,1,1,5,2,2,2,3,3),
(1,4,1,1,5,2,2,2,2,3),
(4,4,1,5,5,6,6,6,6,6),
(4,4,1,5,5,6,7,7,7,6),
(8,9,1,1,1,6,0,0,0,6),
(8,9,9,9,6,6,0,0,6,6),
(8,9,9,0,6,6,0,0,6,6),
(8,9,9,0,0,0,0,0,0,0),
(8,9,9,9,0,0,0,0,0,0))
easy3BoardObj = tb.board(easy3)
cspEasy3=bt.CSP(easy3)
solution=cspEasy3.backtracking_search()
print('Easy 3')
easy3BoardObj.print_board(solution.vals.values())

med1= ((1,1,1,2,2,2,2,2,3,3),
(1,1,1,2,4,4,4,4,3,3),
(1,1,2,2,5,4,4,3,3,3),
(1,6,2,5,5,5,4,3,3,3),
(1,6,2,2,5,4,4,8,8,8),
(6,6,2,2,2,7,4,9,9,8),
(6,6,2,2,7,7,7,9,8,8),
(6,6,2,2,2,7,9,9,9,8),
(6,6,2,0,0,0,0,9,9,8),
(6,0,0,0,0,0,0,0,9,9))
med1BoardObj = tb.board(med1)
cspMed1 = bt.CSP(med1)
solution= cspMed1.backtracking_search()
print('Medium 1')
med1BoardObj.print_board(solution.vals.values())

hard1=((1,2,2,2,2,2,2,2,2,3),
(1,2,4,4,2,2,5,5,2,3),
(1,2,4,4,4,5,5,5,2,3),
(1,2,2,4,4,5,5,3,3,3),
(1,1,2,6,6,7,7,3,3,3),
(1,1,6,6,6,7,7,7,8,3),
(1,1,6,6,9,9,7,7,8,3),
(1,9,9,9,9,9,9,8,8,8),
(1,9,9,9,9,9,9,9,8,8),
(9,9,9,9,9,9,9,9,8,8))
hard1BoardObj= tb.board(hard1)
cspHard1 = bt.CSP(hard1)
solution = cspHard1.backtracking_search()
print('hard 1')
hard1BoardObj.print_board(solution.vals.values())


print('hard 2')
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


