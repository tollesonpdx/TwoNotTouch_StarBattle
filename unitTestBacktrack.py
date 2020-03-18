import unittest
import backTrack as bt

class TestStringMethods(unittest.TestCase):

    def test_get_region_coords_returns_all_regions(self):
        board = ((0,0,1,1,2,2,2,2),
                 (3,3,3,1,1,2,2,2),
                 (4,4,4,4,1,2,2,2),
                 (4,4,4,4,4,4,2,2),
                 (5,6,6,6,4,4,2,2),
                 (5,6,6,6,6,6,6,6),
                 (5,5,7,7,7,7,6,6),
                 (7,7,7,7,7,7,7,7))
        regionCoords= bt.region_domains(board)
        regions=regionCoords.keys()
        for i in range(0,8):
            self.assertIn(i, regions)

    def test_get_region_coords_returns_correct_coords(self):
        board = ((0,0,1,1,2,2,2,2),
                 (3,3,3,1,1,2,2,2),
                 (4,4,4,4,1,2,2,2),
                 (4,4,4,4,4,4,2,2),
                 (5,6,6,6,4,4,2,2),
                 (5,6,6,6,6,6,6,6),
                 (5,5,7,7,7,7,6,6),
                 (7,7,7,7,7,7,7,7))
        regionCoords= bt.region_domains(board)
        self.assertEqual(regionCoords[0], {(0,0), (0,1)})

    def test_init_var(self):
        vars=bt.init_variables([1,2,3])
        self.assertIn('1A', vars)
        self.assertIn('1B', vars)
        self.assertIn('2A', vars)
        self.assertIn('2B', vars)
        self.assertIn('3A', vars)
        self.assertIn('3B', vars)

    def test_init_assignments(self):
        vars=bt.init_variables([1,2,3])
        assignments=bt.init_assignments(vars)
        self.assertIn('1A', assignments.keys())
        self.assertIn('1B', assignments.keys())
        self.assertIn('2A', assignments.keys())
        self.assertIn('2B', assignments.keys())
        self.assertIn('3A', assignments.keys())
        self.assertIn('3B', assignments.keys())

    def test_init_domains(self):
        board = ((0,0,1,1,2,2,2,2),
                 (3,3,3,1,1,2,2,2),
                 (4,4,4,4,1,2,2,2),
                 (4,4,4,4,4,4,2,2),
                 (5,6,6,6,4,4,2,2),
                 (5,6,6,6,6,6,6,6),
                 (5,5,7,7,7,7,6,6),
                 (7,7,7,7,7,7,7,7))

        regionDomains = bt.region_domains(board)
        X = bt.init_variables(regionDomains.keys())
        D = bt.init_domains(X, regionDomains)
        self.assertIn((0,0), D['0A']) 
        self.assertIn((0,1), D['0A']) 
        self.assertIn((7,7), D['7A']) 
    
    def test_isCompleteReturnsTrueWhenAllKeysHaveVal(self):
        assignment = bt.Assignment({1:'a', 2:3, 4:5}, set())
        self.assertTrue(bt.is_complete(assignment))

    def test_isCompleteReturnsFalseWhenValIsNone(self):
        assignment = bt.Assignment({1:2, 2:None, 4:5}, set())
        self.assertFalse(bt.is_complete(assignment))

    def test_inference_returns_assignments(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0), (0,1)},
        '1B':{(0,0), (0,1)},
        '2A':{(1,0), (1,1)},
        '2B':{(1,0), (1,1)}}
        
        var='1A'

        assignments=bt.Assignment({'1A':(0,1)}, set())

        self.assertIn((0,1), csp.inference(var, assignments))

#---------------------------------------------------------------
#                      constraint function tests
#---------------------------------------------------------------

    def test_getNeighbors(self):
        ns = bt.get_neighbors((1,1))
        self.assertIn((0,0), ns)
        self.assertIn((1,0), ns)
        self.assertIn((2,0), ns)
        self.assertIn((0,1), ns)
        self.assertIn((2,1), ns)
        self.assertIn((0,2), ns)
        self.assertIn((1,2), ns)
        self.assertIn((2,2), ns)

    def test_notTooCloseReturnsTrueWhenValsDifferent(self):
        listOfSets=[(0,0),(2,2),(4,4)]
        self.assertTrue(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsFalseWhenValsSame(self):
        listOfSets=[(1,1),(1,1),(3,3)]
        self.assertFalse(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsFalseWhen3inRow(self):
        listOfSets=[(0,0),(0,3),(0,6)]
        self.assertFalse(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsFalseWhen3inCol(self):
        listOfSets=[(0,0),(3,0),(6,0)]
        self.assertFalse(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsTrueWhen2inRow(self):
        listOfSets=[(0,0),(0,3),(5,5)]
        self.assertTrue(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsTrueWhen2inCol(self):
        listOfSets=[(0,3),(3,3),(6,6)]
        self.assertTrue(bt.notTooClose(listOfSets))

    def test_notTooCloseReturnsTrueWhen1inCol(self):
        listOfSets=[(0,0),(2,2),(4,4)]
        self.assertTrue(bt.notTooClose(listOfSets))

    def test_selectUnassignedVariable(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0)},
        '1B':{(0,0), (0,1)},
        '2A':{(1,0), (1,1)},
        '2B':{(1,0), (1,1)}}
        assignment= bt.Assignment(bt.init_assignments(['1A', '1B', '2A', '2B']), set())
        minVar= csp.select_unassigned_var(assignment)
        self.assertEqual(minVar, '1A')

    def test_getRow(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0)},
        '1B':{(0,0), (0,1)},
        '2A':{(1,0), (1,1)},
        '2B':{(1,0), (1,1)}}

        row= csp.get_row((0,0))
        self.assertSetEqual(row, {(0,0),(0,1)})

    def test_getCol(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0)},
        '1B':{(0,0), (0,1)},
        '2A':{(1,0), (1,1)},
        '2B':{(1,0), (1,1)}}

        row= csp.get_col((0,0))
        self.assertSetEqual(row, {(0,0),(1,0)})

    def test_inferencesReturnsNeighborsAndPosOfNewCoord(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0), (0,1), (0,2)},
        '1B':{(0,0), (0,1), (0,2)},
        '2A':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '2B':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}}

        vars=bt.init_variables([1,2])
        assignments=bt.init_assignments(vars)
        assignment = bt.Assignment(assignments,set())
        assignment.vals['1A']=(0,0)
        inferences = csp.inference('1A', assignment)
        self.assertIn((0,0), inferences)
        self.assertIn((0,1), inferences)
        self.assertIn((1,0), inferences)
        self.assertIn((1,1), inferences)

    def test_inferencesReturnsEightNeighborsAndPosOfNewCoord(self):
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

        csp.X={'1A', '1B', '2A', '2B'}
        csp.D={
        '1A':{(0,0), (0,1), (0,2)},
        '1B':{(0,0), (0,1), (0,2)},
        '2A':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '2B':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}}

        vars=bt.init_variables([1,2])
        assignments=bt.init_assignments(vars)
        assignment = bt.Assignment(assignments,set())
        assignment.vals['2A']=(1,1)
        inferences = csp.inference('2A', assignment)
        self.assertIn((0,0), inferences)
        self.assertIn((0,1), inferences)
        self.assertIn((0,2), inferences)
        self.assertIn((1,0), inferences)
        self.assertIn((1,1), inferences)
        self.assertIn((1,2), inferences)
        self.assertIn((2,0), inferences)
        self.assertIn((2,1), inferences)
        self.assertIn((2,2), inferences)

    def test_inferencesReturnsRowsOfNewCoord(self):
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

        csp.X={'1A', '1B', '2A', '2B', '3A', '3B'}
        csp.D={
        '1A':{(0,0), (0,1), (0,2)},
        '1B':{(0,0), (0,1), (0,2)},
        '2A':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '2B':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '3A':{(3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3), (4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)},
        '3B':{(3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3), (4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)}}

        vars=bt.init_variables([1,2])

        assignments=bt.init_assignments(vars)
        assignment = bt.Assignment(assignments,set())
        assignment.vals['1A']=(0,0)
        assignment.vals['3A']=(0,4)

        inferences = csp.inference( '3A', assignment)
        self.assertIn((0,3), inferences)
        self.assertIn((1,3), inferences)
        self.assertIn((1,4), inferences)
        self.assertIn((0,4), inferences)
        self.assertIn((0,2), inferences)


    def test_inferencesReturnsColOfNewCoord(self):
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

        csp.X={'1A', '1B', '2A', '2B', '3A', '3B'}
        csp.D={
        '1A':{(0,0), (0,1), (0,2)},
        '1B':{(0,0), (0,1), (0,2)},
        '2A':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '2B':{(1,0), (1,1), (1,2), (2,0), (2,1), (2,2)},
        '3A':{(3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3), (4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)},
        '3B':{(3,0), (3,1), (3,2), (3,3), (2,3), (1,3), (0,3), (4,0), (4,1), (4,2), (4,3), (4,4), (3,4), (2,4), (1,4), (0,4)}}

        vars=bt.init_variables([1,2])

        assignments=bt.init_assignments(vars)
        assignment = bt.Assignment(assignments,set())
        assignment.vals['3B']=(0,4)
        assignment.vals['3A']=(4,4)

        inferences = csp.inference( '3A', assignment)
        self.assertIn((2,4), inferences)

    #def test_coordsW

#   def test_upper(self):
#       self.assertEqual('foo'.upper(), 'FOO')

#   def test_isupper(self):
#       self.assertTrue('FOO'.isupper())
#       self.assertFalse('Foo'.isupper())

#   def test_split(self):
#       s = 'hello world'
#       self.assertEqual(s.split(), ['hello', 'world'])
#       
#       # check that s.split fails when the separator is not a string
#       with self.assertRaises(TypeError):
#           s.split(2)

if __name__ == '__main__':
    unittest.main()