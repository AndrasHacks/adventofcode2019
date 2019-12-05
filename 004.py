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
        self.assertEqual(run_int_code([1, 1, 1, 4, 99, 5, 6, 0, 99]),
                [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def get_code(self):
        f = open(r'002.input.txt', 'r')
        ls = f.readlines()
        s = ls[0]
        code = s.replace('\n', '').split(',')
        for i in range(len(code)):
            code[i] = int(code[i])
        f.close()
        return code

    def test_solution(self):
        for noun in range(0, 100):
            for verb in range(0, 100):
                code = self.get_code()
                code[1] = noun
                code[2] = verb
                try:
                    result = run_int_code(code)
                    if result[0] == 19690720:
                        print('noun', noun, 'verb', verb)
                        print(100 * noun + verb)
                        break
                except:
                    continue
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
