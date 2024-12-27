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


def parse(input_str, part2=False):
    result = []
    pattern = r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)"""
    matches = re.findall(pattern, input_str)

    for match in matches:
        machine = Machine(int(match[0]), int(match[1]), int(match[2]), int(match[3]), int(match[4]), int(match[5]))
        if part2:
            machine.tx += 10000000000000
            machine.ty += 10000000000000
        result.append(machine)
    return result


if __name__ == '__main__':

    # real_input = open("input13.txt").read()
    machines = parse(test_input, part2=True)

    mins = []
    for machine in machines:
        min_cost = math.inf
        max_a_presses = machine.tx // machine.ax
        for a_press in range(0, max_a_presses + 1):
            x_remainder = machine.tx - (machine.ax * a_press)
            y_remainder = machine.ty - (machine.ay * a_press)
            if x_remainder % machine.bx == 0 and y_remainder % machine.by == 0 and (
                    x_remainder / machine.bx == y_remainder / machine.by):
                b_press = x_remainder // machine.bx
                cost = 3 * a_press + b_press
                min_cost = min(min_cost, cost)

        mins.append(min_cost)
        print(f"machine {machine} has min {min_cost}")
    print(sum([x for x in mins if x != math.inf]))
