# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
from itertools import product

import math
from collections import deque

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

dirpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]


def solve(steps, keypad):
    rows, cols = len(keypad), len(keypad[0])
    key2loc = {}
    allowed_positions = set()
    for r in range(rows):
        for c in range(cols):
            key = keypad[r][c]
            if key is not None:
                key2loc[key] = (r, c)
                allowed_positions.add((r, c))

    paths = {}
    for x in key2loc:
        for y in key2loc:
            if x == y:
                paths[(x, y)] = ["A"]
                continue
            possible_paths = []
            q = deque([(key2loc[x], "")])
            optimal = math.inf
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in (r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">"):
                    if (nr, nc) not in allowed_positions: continue
                    if (nr, nc) == key2loc[y]:
                        if len(moves) + 1 > optimal:
                            break
                        optimal = len(moves) + 1
                        possible_paths.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:  # breaks propagate
                    continue
                break
            paths[(x, y)] = possible_paths

    result = []
    for first, second in zip("A" + steps, steps):
        result.append(paths[first, second])
    return [''.join(x) for x in product(*result)]

test_input = """\
029A
980A
179A
456A
379A"""

if __name__ == '__main__':
    # input_string = test_input
    input_string= open("input21.txt").read()

    total = 0
    for line in input_string.splitlines():
        robot1_options = solve(line, numpad)

        robot2_options = []
        for path in robot1_options:
            robot2_options.extend(solve(path, dirpad))
        optimal = min(map(len, robot2_options))
        robot2_options = [r for r in robot2_options if len(r) == optimal]
        # print(robot2_options)

        robot3_options = []
        for path in robot2_options:
            robot3_options.extend(solve(path, dirpad))
        optimal = min(map(len, robot3_options))
        robot3_options = [r for r in robot3_options if len(r) == optimal]
        # print("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A" in robot3_options)
        complexity = len(robot3_options[0])
        numeric = int(line[:-1])
        result = complexity * numeric
        print(f"{complexity}x{numeric} = {result}")
        total += result
    print(total)