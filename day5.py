def process(comm):
    program = comm.split(',')
    program = map(lambda c: int(c), program)
    ip = 0
    while ip < len(program):
        full_command = str(program[ip]).rjust(5, '0')
        # print(full_command) 
        if int(full_command[-2:]) < 3:
           param1 = program[ip + 1] if full_command[-3] == "1" else program[program[ip + 1]]
           param2 = program[ip + 2] if full_command[-4] == "1" else program[program[ip + 2]]
        if full_command[-2:] == '01':
           program[program[ip + 3]] = param1 + param2
           ip += 4
        elif  full_command[-2:] == '02':
           program[program[ip + 3]] = param1 * param2 
           ip += 4
        elif full_command[-2:] == '03':
            program[program[ip+1]] = int(input())
            ip += 2
        elif full_command[-2:] == '04':
            if full_command[-3] == "1":
                print(program[ip + 1])
            else:
                print(program[program[ip+1]])
            ip += 2
        elif full_command[-2:] == '99':
            break
        else:
            raise Exception('Not a correct opcode!')
    program = map(lambda c: str(c), program)
    return ','.join(program)
