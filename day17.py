test_input = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""

# If register C contains 9, the program 2,6 would set register B to 1.
# If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
test_2 = """\
Register A: 10
Register B: 0
Register C: 0

Program: 5,0,5,1,5,4
"""
# If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
# If register B contains 29, the program 1,7 would set register B to 26.
# If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.

test_part2 = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""


def run_program(a, b, c, program, solve_mode=False):
    program = [x for x in program]
    output = []
    ptr = 0
    while True:
        # print(f'Ptr: {ptr}')
        op_code = program[ptr]
        literal_operand = program[ptr + 1]
        if literal_operand <= 3:
            combo_operand = literal_operand
        elif literal_operand == 4:
            combo_operand = a
        elif literal_operand == 5:
            combo_operand = b
        elif literal_operand == 6:
            combo_operand = c
        elif literal_operand == 7:
            combo_operand = None  # could use as literal
        else:
            raise ValueError(f'Unknown combo operator for operand {literal_operand}')
        # print(op_code, operand)
        if op_code == 0:
            a = a // (2 ** combo_operand)
            # The adv instruction (opcode 0) performs division.
            # The numerator is the value in the A register.
            # The denominator is found by raising 2 to the power of the instruction's combo operand.
            # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.)
            # The result of the division operation is truncated to an integer and then written to the A register.
        elif op_code == 1:
            b = b ^ literal_operand
            # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal
            # operand, then stores the result in register B.
        elif op_code == 2:
            b = combo_operand % 8
            # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only
            # its lowest 3 bits), then writes that value to the B register.
        elif op_code == 3:
            if a == 0:
                pass
            else:
                # print(f'Advancing PTR to ... {a}')
                ptr = literal_operand
                continue
            # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not
            # zero, it jumps by setting the instruction pointer to the value of its literal operand; if this
            # instruction jumps, the instruction pointer is not increased by 2 after this instruction.
        elif op_code == 4:
            b = b ^ c
            # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the
            # result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
        elif op_code == 5:
            output.append(combo_operand % 8)
            # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that
            # value. (If a program outputs multiple values, they are separated by commas.)
        elif op_code == 6:
            b = a // (2 ** combo_operand)
            # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored
            # in the B register. (The numerator is still read from the A register.)
        elif op_code == 7:
            c = a // (2 ** combo_operand)
            # The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored
            # in the C register. (The numerator is still read from the A register.)
        else:
            raise ValueError(f"Unknwon op_code {op_code}")

        if solve_mode:
            for x, y in zip(program, output):
                if x != y:
                    raise RuntimeError('Solve not found (fail fast check) - try again')

        if ptr == len(program) - 2:
            break
        else:
            ptr += 2
    if solve_mode and program != output:
        raise RuntimeError('Solve not found (final check) - try again')
    return output


def find(prog, ans):
    """ Full credit HyperNeutrino"""
    print(prog)
    if prog == []: return ans
    for t in range(8):
        a = ans << 3 | t
        b = a % 8
        b = b ^ 2
        c = a >> b
        # b = b ^ c
        # b = b ^ 3
        # a = a >> 3
        b = b ^ 7
        b = b ^ c
        if b % 8 == prog[-1]:
            sub = find(prog[:-1], a)
            if sub is None: continue
            return sub


if __name__ == '__main__':
    # input_str = test_part2
    input_str = open('input17.txt').read()

    a, b, c, space, p = input_str.splitlines()
    a = int(a.split()[2])
    b = int(b.split()[2])
    c = int(c.split()[2])
    program = [int(x) for x in p.split()[1].split(',')]
    output = run_program(a, b, c, program, solve_mode=False)

    # print(','.join(str(x) for x in output))

    # a_to_try = 117430
    # while True:
    #     try:
    #         # print(f'Attempting {a_to_try}')
    #         output = run_program(a_to_try, b, c, program, solve_mode=True)
    #         print(f'Success: {a_to_try}')
    #         break
    #     except Exception as e:
    #         a_to_try += 1
    #         continue
    print(find(program, 0))

# part 2....
# Register A: 27334280
# Register B: 0
# Register C: 0
#
# Program:
# 2,4,   y
# 1,2,   y
# 7,5,   y
# 0,3,   a
# 1,7,   a
# 4,1,   a
# 5,5,   y
# 3,0    y
# b = b % 8
# b = b ^ 2
# c = a >> b
# a = a >> 3
# b = b ^ 7
# b = b ^ c
# out(b % 8)
# if a != 0: jump 0
