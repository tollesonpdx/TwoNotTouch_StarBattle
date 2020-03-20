import unittest
from twoNotTouch import boardList
from ac3 import ac_csp
import math

class ac3_test(unittest.TestCase):
    '''
    This works with any subset of boardList or with a hard coded board
    '''

    def test_vars(self):
        # board = boardList.a
        board = boardList.b
        Testac_CSP = ac_csp(board)
        vars = Testac_CSP.vars
        expected = len(board) * 2  # we would have to hard code this to 1 to make it pass a test for 1 star
        result = len(vars)
        self.assertEqual(expected, result)
        # print("This has generated a list of" int(len(vars))

    def test_domain(self):
        # board = boardList.a
        board = boardList.b
        Testac_CSP = ac_csp(board)
        domain = Testac_CSP.domain
        expected = len(board) * len(board)
        result = len(domain)
        self.assertEqual(expected, result)
        # print("This has generated", len(domain), "coordinates.  It should generate", int(math.pow(len(board), 2), "coordinates."
        # print(domain)

    def test_arcs(self):
        # board = boardList.a
        board = boardList.b
        Testac_CSP = ac_csp(board)
        domain = Testac_CSP.domain
        arcs = Testac_CSP.arcs
        expected = (math.pow(len(domain), 2) - len(domain))
        result = len(arcs)
        self.assertEqual(expected, result)
        # print("This has generated", len(arcs), "arcs.  It should generate", int(math.pow(len(vars), 2) - len(vars)) , "arcs.")
        # print(arcs)

if __name__ == "__main__":
    unittest.main()