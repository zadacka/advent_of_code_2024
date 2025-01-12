# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
from collections import deque
from functools import cache

import math
from itertools import product


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

def compute_sequences(keypad):
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
                for nr, nc, nm in (r - 1, c, "^"), (r + 1, c, "v"), (r, c - 1, "<"), (r, c + 1, ">"):
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
    return paths


numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]
numpad_paths = compute_sequences(numpad)

dirpad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]
dirpad_paths = compute_sequences(dirpad)
dirpad_path_lengths = {k: len(v[0]) for k, v in dirpad_paths.items()}


def solve(steps, keypad_paths):
    result = []
    for first, second in zip("A" + steps, steps):
        result.append(keypad_paths[first, second])
    return [''.join(x) for x in product(*result)]

@cache
def comput_length(x, y, depth=2):
    if depth == 1:
        return dirpad_path_lengths[x, y]
    optimal = math.inf
    for path in dirpad_paths[x, y]:
        length = 0
        for a, b in zip("A" + path, path):
            length += comput_length(a, b, depth - 1)
        optimal = min(optimal, length)
    return optimal

test_input = """\
029A
980A
179A
456A
379A"""

if __name__ == '__main__':
    # input_string = test_input
    input_string = open("input21.txt").read()

    total = 0
    for line in input_string.splitlines():
        inputs = solve(line, numpad_paths)

        optimal = math.inf
        for path in inputs:
            length = 0
            for a, b in zip("A" + path, path):
                length += comput_length(a, b, depth=25)
            optimal = min(optimal, length)
        print(optimal)
        numeric = int(line[:-1])
        result = optimal * numeric
        print(f"{optimal}x{numeric} = {result}")
        total += result
    print(total)
