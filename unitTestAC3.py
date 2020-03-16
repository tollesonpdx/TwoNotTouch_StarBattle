import unittest
from twoNotTouch import boardList
from ac3 import csp

class ac3_test(unittest.TestCase):
    '''
    This works with any subset of boardList or with a hard coded board
    '''


    def test_board(self):
        board = boardList.a
        #  board = boardList.b
        TestCSP = csp(board)
        vars = TestCSP.get_vars(board)
        arcs = TestCSP.make_arcs()
        domains = []
        constraints = {}
        expected = len(board) * len(board)
        result = len(vars)
        self.assertEqual(expected, result)
        print("Created: ", len(vars), "coordinates")
        print(vars)
        print(arcs)

if __name__ == "__main__":
    unittest.main()