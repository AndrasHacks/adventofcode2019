import unittest
five = __import__('005')

class test(unittest.TestCase):
    def test_make_wire(self):
        wire = five.Wire('R8,L10,D5')
        self.assertEqual(wire.path[0], 'R8')

if __name__ == '__main__':
    unittest.main()    
