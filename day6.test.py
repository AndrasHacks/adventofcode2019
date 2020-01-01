import unittest
uom = __import__('day6')

class UniversalOrbitMapTest(unittest.TestCase):

# Count all direct orbits

# 1) Create a dictionary with all the orbtting planets with all the
#       planets they are orbitting
#               as we add the items increment the dirct orbits!

    EXAMPLE = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
    EXAMPLE2 = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN"

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

# 1. Get YOU - COM, SAN - COM routes
# 2. For all hop count the distance from YOU / SAN
# 3. GET the one which is in both with the least distance

    def x_test_get_route_from_A_to_B(self):
        uni_map = 'A)B\nB)C\nC)D'
        route = uom.get_route(uom.get_dict(uni_map), 'D', 'A')
        self.assertEqual(route, ['D', 'C', 'B', 'A'])

    def test_example2(self):
        dict_res = uom.get_dict(self.EXAMPLE2)
        you = uom.get_route(dict_res, 'YOU', 'COM')
        santa = uom.get_route(dict_res, 'SAN', 'COM')
        both = set(you) & set(santa)
        in_both = map(lambda item: {'name': item, 'value': you.index(item) + santa.index(item)}, list(both))
        min_ind = 0
        for ind in range(1, len(in_both)):
            if in_both[ind]['value'] < in_both[min_ind]['value']:
                min_ind = ind
        bridge = in_both[min_ind]
        orbit_transfer_count = uom.get_orbit_count(dict_res, 'YOU', bridge['name']) + uom.get_orbit_count(dict_res, 'SAN', bridge['name']) - 2
        self.assertEqual(orbit_transfer_count, 4)

    def test_day6_part2(self):
        f = open(r'day6.input.txt', 'r')
        dict_res = uom.get_dict(f.read())
        you = uom.get_route(dict_res, 'YOU', 'COM')
        santa = uom.get_route(dict_res, 'SAN', 'COM')
        both = set(you) & set(santa)
        in_both = map(lambda item: {'name': item, 'value': you.index(item) + santa.index(item)}, list(both))
        min_ind = 0
        for ind in range(1, len(in_both)):
            if in_both[ind]['value'] < in_both[min_ind]['value']:
                min_ind = ind
        bridge = in_both[min_ind]
        orbit_transfer_count = uom.get_orbit_count(dict_res, 'YOU', bridge['name']) + uom.get_orbit_count(dict_res, 'SAN', bridge['name']) - 2
        print(orbit_transfer_count)

if __name__ == '__main__':
    unittest.main()
