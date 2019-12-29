import unittest
uom = __import__('day6')

class UniversalOrbitMapTest(unittest.TestCase):

# Count all direct orbits

# 1) Create a dictionary with all the orbtting planets with all the
#       planets they are orbitting
#               as we add the items increment the dirct orbits!

    EXAMPLE = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"

    def test_B_orbits_A(self):
        result = uom.get_dict('A)B')
        self.assertEqual(len(result.keys()), 1)
        self.assertTrue('B' in result.keys())
        self.assertEqual(len(result['B']), 1)
        self.assertTrue('A' in result['B'])

    def test_B_and_C_orbits_A(self):
        result = uom.get_dict('A)B\nA)C')
        self.assertTrue('A' in result['B'] and 'A' in result['C'])

    def test_A_orbits_B_and_A_orbits_C(self):
        result = uom.get_dict('B)A\nC)A')
        self.assertTrue('B' in result['A'] and 'C' in result['A'])

    def test_given_example(self):
        dict_res = uom.get_dict(self.EXAMPLE)
        self.assertEqual(len(dict_res.keys()), 11)
    
    def test_simple_count_orbits(self): 
        dict_res = uom.get_dict('COM)B\nB)C')
        orbit_count = uom.get_orbit_count(dict_res, 'C')
        self.assertEqual(2, orbit_count)

    def test_given_example_count_orbits(self):
        dict_res = uom.get_dict(self.EXAMPLE)
        orbit_count = uom.get_orbit_count(dict_res, 'L')
        self.assertEqual(7, orbit_count) 

    def test_count_all_for_given_example(self):
        dict_res = uom.get_dict(self.EXAMPLE)
        self.assertEqual(42, uom.get_check_sum(dict_res))

    def test_day6_part1(self):
        f = open(r'day6.input.txt', 'r')
        dict_res = uom.get_dict(f.read())
        print(uom.get_check_sum(dict_res))

if __name__ == '__main__':
    unittest.main()
