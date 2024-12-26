import math

import re

test_input = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""


class Machine:

    def __init__(self, ax, ay, bx, by, tx, ty):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.tx = tx
        self.ty = ty
        super().__init__()

    def __repr__(self):
        return f"Machine({self.ax}, {self.ay}, {self.bx}, {self.by}, {self.tx}, {self.ty})"

def parse(input_str):
    result = []
    pattern = r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)"""
    matches = re.findall(pattern, input_str)
    for match in matches:
        result.append(Machine(int(match[0]), int(match[1]), int(match[2]), int(match[3]), int(match[4]), int(match[5])))
    return result

if __name__ == '__main__':

    real_input = open("input13.txt").read()
    machines = parse(real_input)

    mins = []
    for machine in machines:
        min_cost = math.inf
        for a_press in range(0, 101):
            for b_press in range(0, 101):
                x = machine.ax * a_press + machine.bx * b_press
                y = machine.ay * a_press + machine.by * b_press
                if machine.tx == x and machine.ty == y:
                    min_cost = min(min_cost, a_press * 3 + b_press)
                elif x > machine.tx or y > machine.ty:
                    break
        mins.append(min_cost)
        print(f"machine {machine} has min {min_cost}")
    print(sum([x for x in mins if x != math.inf]))