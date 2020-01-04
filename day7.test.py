import unittest
int_code_comp = __import__('day7')

class IntCodeComputerTest(unittest.TestCase):
    # opcodes can be: 1, 2, 99
    # 1 - adds, 2 - multiplies, 99 - halts immediately

    # 1,0,0,3,99 --> adds numbers from the first position,
    # stores it in the third place and halts

    def create_input_fn(self, value):
        def input():
            return value
        return input

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

    def test_get_text(self):
        prog = '3,3,1,0,2,5,99'
        result = int_code_comp.process(prog, self.create_input_fn(2))
        self.assertEqual(result, '3,3,1,2,2,2,99')

    def test_print_text(self):
        result = int_code_comp.process('4,0,99')
        # 4 should be printed out

    def test_print_function_pass(self):
        out_buff = ''
        def print_fn(to_print):
            nonlocal out_buff
            out_buff += str(to_print) + '\n'
        result = int_code_comp.process('4,2,99', input, print_fn)
        print(out_buff)

    def test_input_output_buffer(self):
        prog = '3,1,4,1,3,1,4,1,99'
        in_buff = '4\n2'
        in_ctr = 0
        out_buff = ''
        def in_fn():
            nonlocal in_ctr
            nonlocal in_buff
            inputs = list(map(lambda i: int(i), in_buff.split('\n')))
            ret_val = inputs[in_ctr]
            in_ctr += 1
            return ret_val
        def out_fn(to_print):
            nonlocal out_buff
            out_buff += str(to_print) + '\n'
        result = int_code_comp.process(prog, in_fn, out_fn)
        print(out_buff)

    def test_param_modes(self):
        result = int_code_comp.process('1002,4,3,4,33')
        self.assertEqual(result, '1002,4,3,4,99')

    def test_param_modes_add(self):
        result = int_code_comp.process('11001,4,1,4,98')
        self.assertEqual(result, '11001,4,1,4,99')

    def test_day5_part1(self):
        in_prg = open(r'day5.input.text', 'r')
        day5_part1_input = self.create_input_fn(1)
        prog = in_prg.readlines()[0]
        result = int_code_comp.process(prog, day5_part1_input)
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

    def test_get_phase_strings(self):
        phase_strings = int_code_comp.get_amplifier_phase_strings()
        self.assertEqual(5**5, len(phase_strings))
        self.assertEqual('00000', phase_strings[0])
        self.assertEqual('44444', phase_strings[5**5 - 1])

    def test_get_amplifier(self):
        amplifier = int_code_comp.Amplifier(0,0)
        result = amplifier.process('1,0,0,3,99')
        self.assertEqual('', result['print_res'])
        self.assertEqual('1,0,0,2,99', result['prg_res'])

    def test_amplifier_inut_and_phase(self):
        amplifier = int_code_comp.Amplifier(2,4)
        program = '3,0,3,3,4,0,4,3,99'
        result = amplifier.process(program)
        self.assertEqual('4,0,3,2,4,0,4,3,99', result['prg_res'])
        self.assertEqual('4\n2', result['print_res'])

    def test_amplifier_given_example(self):
        amplifier = int_code_comp.Amplifier(0,4)
        prog = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        result = amplifier.process(prog)
        self.assertEqual('4', result['print_res'])

    def x_test_get_amplifier_chain(self):
        amplifier_chain = int_code_comp.AmplifierChain(1, '00000')
        result = amplifier_chain.process('1,0,0,3,99')
        self.assertEqual(result['prg_res'], '1,0,0,2,99')
        self.assertEqual(result['print_res'], '')

    def test_given_example(self):
        prog = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        phases = int_code_comp.get_amplifier_phase_strings()
        results = []
        for i in range(len(phases)):
            amp_chain = int_code_comp.AmplifierChain(0, phases[i])
            result = amp_chain.process(prog)
            results.append(int(result['print_res']))
        self.assertEqual(max(results), 43210)

if __name__ == '__main__':
    unittest.main()
