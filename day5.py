def process(comm):
    program = comm.split(',')
    program = map(lambda c: int(c), program)
    ip = 0
    while ip < len(program):
        full_command = str(program[ip]).rjust(5, '0')
        op_code = full_command[-2:] 
        p1_im = full_command[-3] == '1'
        p2_im = full_command[-4] == '1'
        if int(op_code) in [1, 2, 7, 8]:
           param1 = program[ip + 1] if p1_im else program[program[ip + 1]]
           param2 = program[ip + 2] if p2_im else program[program[ip + 2]]
        if op_code == '01':
           program[program[ip + 3]] = param1 + param2
           ip += 4
        elif  op_code == '02':
           program[program[ip + 3]] = param1 * param2 
           ip += 4
        elif op_code == '03':
            program[program[ip+1]] = int(input())
            ip += 2
        elif op_code == '04':
            if full_command[-3] == "1":
                print(program[ip + 1])
            else:
                print(program[program[ip+1]])
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
                if ip > len(program):
                    print(ip, full_command)
                    raise Exception('Instruction pointer overflow!')
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
                if ip > len(program):
                    print(ip, full_command)
                    raise Exception('Instruction pointer overflow!')
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
