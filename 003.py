import unittest

def run_int_code(code):
    ptr = 0
    while  ptr < len(code):
        if code[ptr] == 1:
            code[code[ptr + 3]] = code[code[ptr + 1]] + code[code[ptr + 2]]
        elif code[ptr] == 2:
            code[code[ptr + 3]] = code[code[ptr + 1]] * code[code[ptr + 2]]
        elif code[ptr] == 99:
            break;
        ptr = ptr + 4
    return code

class TestSecondDayFirst(unittest.TestCase):
    def test_basic_scenario(self):
        self.assertEqual(run_int_code([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]), [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50] )

    def test_1(self):
        self.assertEqual(run_int_code([1, 1, 1, 4, 99, 5, 6, 0, 99]), [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_solution(self):
        f = open(r'002.input.txt', 'r')
        ls = f.readlines()
        s = ls[0]
        code = s.replace('\n', '').split(',')
        for i in range(len(code)):
            code[i] = int(code[i])
        print(run_int_code(code))
        f.close()
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
