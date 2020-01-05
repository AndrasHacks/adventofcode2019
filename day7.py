def process(command, input_fn = input, print_fn = print):
    program = command.split(',')
    program = list(map(lambda c: int(c), program))
    ip = 0
    while ip < len(program):
        full_command = str(program[ip]).rjust(5, '0')
        op_code = full_command[-2:]
        p1_im = full_command[-3] == '1'
        p2_im = full_command[-4] == '1'

        # check immediate / position mode for:
        # add, mul, jmp_less_then, jmp_equals
        if int(op_code) in [1, 2, 7, 8]:
           param1 = program[ip + 1] if p1_im else program[program[ip + 1]]
           param2 = program[ip + 2] if p2_im else program[program[ip + 2]]
        if op_code == '01':
           program[program[ip + 3]] = param1 + param2
           ip += 4
        elif op_code == '02':
           program[program[ip + 3]] = param1 * param2
           ip += 4
        elif op_code == '03':
            program[program[ip+1]] = int(input_fn())
            ip += 2
        elif op_code == '04':
            if full_command[-3] == "1":
                print_fn(program[ip + 1])
            else:
                print_fn(program[program[ip+1]])
            ip += 2
        elif op_code == '05':
            jumps = False
            jumps = p1_im and program[ip + 1] != 0
            jumps = jumps or not p1_im and program[program[ip + 1]] != 0
            if jumps:
                if p2_im:
                    ip = program[ip + 2]
                else:
                    ip = program[program[ip + 2]]
                raise_memory_exception(ip, full_command, len(program))
            else:
                ip += 3
        elif op_code == '06':
            jumps = False
            jumps = p1_im and program[ip + 1] == 0
            jumps = jumps or not p1_im and program[program[ip + 1]] == 0
            if jumps:
                if p2_im:
                    ip = program[ip + 2]
                else:
                    ip = program[program[ip + 2]]
                raise_memory_exception(ip, full_command, len(program))
            else:
                ip += 3
        elif op_code == '07':
            jumps = param1 < param2
            program[program[ip + 3]] = 1 if jumps else 0
            ip += 4
        elif op_code == '08':
            jumps = param1 ==  param2
            program[program[ip + 3]] = 1 if jumps else 0
            ip += 4
        elif op_code == '99':
            break
        else:
            raise Exception(full_command + ' is not a correct opcode!')
    program = map(lambda c: str(c), program)
    return ','.join(program)

def raise_memory_exception(instruction_pointer, command, prog_len):
    if instruction_pointer > prog_len:
        print(instruction_pointer, full_command)
        raise Exception('Instruction pointer overflow!')

def get_amplifier_phase_strings():
    phase_strings = []
    for decimal in range(5**5):
        converted = convert_number(decimal, 5)
        if len(list(converted)) == len(set(list(converted))):
            phase_strings.append(convert_number(decimal, 5))
    return phase_strings

def convert_number(decimal, base):
    converted = ''
    while decimal > 0:
        converted = str(decimal % base) + converted
        decimal = decimal // base
    return converted.rjust(base, '0')

class Amplifier():

    def __init__(self, inp, phase):
        self.input = inp
        self.phase = phase

    def process(self, program):
        input_buffer = str(self.phase) + '\n' + str(self.input)
        input_ctr = 0
        def input_fn():
            nonlocal input_buffer
            nonlocal input_ctr
            to_input = input_buffer.split('\n')[input_ctr]
            input_ctr += 1
            return to_input

        out_buffer = ''
        def out_fn(to_out):
            nonlocal out_buffer
            if out_buffer == '':
                out_buffer = str(to_out)
            else:
                out_buffer += '\n' + str(to_out)
        prg_res = process(program, input_fn, out_fn)
        return {'prg_res': prg_res, 'print_res': out_buffer}

class AmplifierChain():

    def __init__(self, inp, phases):
       self.input = inp
       self.phases = phases

    def process(self, program):
        amp_input = self.input
        result = None
        for i in range(5):
            amp = Amplifier(amp_input, self.phases[i])
            result = amp.process(program)
            amp_input = result['print_res']
        return result



