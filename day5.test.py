import unittest
int_code_comp = __import__('day5')

class IntCodeComputerTest(unittest.TestCase):
    # opcodes can be: 1, 2, 99
    # 1 - adds, 2 - multiplies, 99 - halts immediately

    # 1,0,0,3,99 --> adds numbers from the first position,
    # stores it in the third place and halts

    def test_adds_and_halts(self):
       result = int_code_comp.process('1,0,0,3,99')
       self.assertEqual(result, '1,0,0,2,99')

    def test_muls_and_halts(self):
        result = int_code_comp.process('2,0,4,3,99')
        self.assertEqual(result, '2,0,4,198,99')

    def test_adds_and_muls_and_halts(self):
        result = int_code_comp.process('1,0,0,3,2,3,3,7,99')
        self.assertEqual(result, '1,0,0,2,2,3,3,4,99')

    def test_halt_in_time(self):
        result = int_code_comp.process('1,0,0,3,99,0,0,0,2,3,3,3')
        self.assertEqual(result, '1,0,0,2,99,0,0,0,2,3,3,3')

    def test_given_example(self):
        start_prog = '1,9,10,3,2,3,11,0,99,30,40,50'
        result = int_code_comp.process(start_prog)
        self.assertEqual(result, '3500,9,10,70,2,3,11,0,99,30,40,50')

    def test_day2(self):
        in_prg = open(r'002.input.txt', 'r')
        result = int_code_comp.process(in_prg.readlines()[0])
        self.assertEqual(result.split(',')[0], '4714701')
        in_prg.close()

    def x_test_get_text(self):
        # insert '2'
        result = int_code_comp.process('3,3,1,0,2,5,99')
        self.assertEqual(result, '3,3,1,2,2,2,99')

    def test_print_text(self):
        result = int_code_comp.process('4,0,99')
        # 4 should be printed out

    def test_param_modes(self):
        result = int_code_comp.process('1002,4,3,4,33')
        self.assertEqual(result, '1002,4,3,4,99')

    def test_param_modes_add(self):
        result = int_code_comp.process('11001,4,1,4,98')
        self.assertEqual(result, '11001,4,1,4,99')

    def test_day5_part1(self):
        in_prg = open(r'day5.input.text', 'r') 
        result = int_code_comp.process(in_prg.readlines()[0])
        in_prg.close()

    def test_jump_if_true_position_jumps(self):
        prg = '5,0,3,4,99'
        result = int_code_comp.process(prg)
        self.assertEqual(result, '5,0,3,4,99')

    def test_jump_if_true_position_no_jump(self):
        prg = '5,2,0,99'
        result = int_code_comp.process(prg)
        self.assertEqual(result, '5,2,0,99')
 
    def test_jump_if_true_immideate_no_jump(self):
        prg = '1105,0,7,1,0,0,6,99'
        result = int_code_comp.process(prg)
        self.assertEqual(result, '1105,0,7,1,0,0,2210,99')

    def test_jump_if_true_immideate_jumps(self):
        prg = '4,0,1105,1,9,1,0,0,8,99'
        result = int_code_comp.process(prg)
        self.assertEqual(result, '4,0,1105,1,9,1,0,0,8,99')
    

if __name__ == '__main__':
    unittest.main()
