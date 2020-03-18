import unittest
from twoNotTouch import boardList
from ac3 import ac_csp
import math

class ac3_test(unittest.TestCase):
    '''
    This works with any subset of boardList or with a hard coded board
    '''


    def test_board(self):
        board = boardList.a
        #  board = boardList.b
        Testac_CSP = ac_csp(board)
        vars = Testac_CSP.get_vars(board)
        arcs = Testac_CSP.make_arcs()
        domains = []
        constraints = {}
        expected = len(board) * len(board)
        result = len(vars)
        self.assertEqual(expected, result)
        # print("Created: ", len(vars), "coordinates")
        # print(vars)
        expected = (math.pow(len(vars), 2) - len(vars))
        result = len(arcs)
        self.assertEqual(expected, result)
        # print("This has generated", len(arcs), "arcs.  It should generate", int(math.pow(len(vars), 2) - len(vars)) , "arcs.")
        # print(arcs)

if __name__ == "__main__":
    unittest.main()