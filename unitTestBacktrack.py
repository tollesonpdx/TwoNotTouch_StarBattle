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
        self.assertTrue(bt.is_complete({1:'a', 2:3, 4:5}))

    def test_isCompleteReturnsFalseWhenValIsNone(self):
        self.assertFalse(bt.is_complete({1:2, 2:None, 4:5}))

    def test_duck(self):
        duck = bt.Duck(bill='wide orange', tail='long')
        self.assertEqual(duck.bill, 'wide orange')


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