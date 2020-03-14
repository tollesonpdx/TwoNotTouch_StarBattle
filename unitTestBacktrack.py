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
        regionCoords= bt.get_region_coords(board)
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
        regionCoords= bt.get_region_coords(board)
        self.assertEqual(regionCoords[0], {(0,0), (0,1)})

    def test_init_var(self):
        vars=bt.init_variables([1,2,3])
        self.assertIn('1A', vars.keys())
        self.assertIn('1B', vars.keys())
        self.assertIn('2A', vars.keys())
        self.assertIn('2B', vars.keys())
        self.assertIn('3A', vars.keys())
        self.assertIn('3B', vars.keys())

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