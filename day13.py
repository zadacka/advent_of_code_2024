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

    real_input = open("input13.txt").read()
    machines = parse(real_input, part2=True)

    total = 0
    for m in machines:

        # a_presses * m.ax + b_presses * m.bx == m.tx
        # a_presses * m.ay + b_presses * m.by == m.ty

        # a_presses * m.ax * m.by + (b_presses * m.bx * m.by) == m.tx * m.by
        # a_presses * m.ay * m.bx + (b_presses * m.by * m.bx) == m.ty * m.bx

        # a_presses ( m.ax * m.by - m.ay * m.bx) = m.tx * m.by - m.ty * m.bx
        a_presses = (m.tx * m.by - m.ty * m.bx) / (m.ax * m.by - m.ay * m.bx)
        b_presses = (m.tx - a_presses * m.ax) / m.bx
        if a_presses % 1 == 0 and b_presses % 1 == 0:
            total += int(a_presses * 3 + b_presses)
            print(f"A {a_presses} and B {b_presses} for machine: {m}")
        else:
            print(f"No solution for machine: {m}")

    print(f"{total}")