test_input = """\
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

test_input2 = """\
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

if __name__ == '__main__':
    # input_str = test_input
    # input_str = test_input2
    input_str = open("input16.txt").read()
    grid = [list(line) for line in input_str.splitlines()]
    gridmap = dict()

    start = None
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            gridmap[(r, c)] = char
            if char == 'S':
                start = (r, c)
    del c, char, r, input_str, test_input,

    forward_left_right = {'N': 'WEN', 'S': 'WES', 'E': 'NSE', 'W': 'NSW'}
    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    stack = []  # position, direction, visited, score
    scores = []

    best_route = dict()

    (r, c), direction, visited, score = start, 'E', set(), 0
    try_popstack = False
    while True:

        if (r, c) not in best_route:
            best_route[(r, c)] = score
        elif score < best_route[(r, c)]:
            best_route[(r, c)] = score
        else:
            try_popstack = True

        if gridmap[(r, c)] == 'E':
            print(f"Made it! {score}")
            scores.append(score)
            try_popstack = True

        if gridmap[(r, c)] == '#':
            try_popstack = True

        if try_popstack:
            if stack:
                (r, c), direction, visited, score = stack.pop()
                try_popstack = False
                continue
            else:
                break

        print(r, c)
        visited.add((r, c))

        lrf = forward_left_right[direction]

        for dir in lrf[0], lrf[1]:
            dr, dc = directions[dir]
            nr, nc = r + dr, c + dc
            if gridmap[(nr, nc)] == '.' and (nr, nc) not in visited:
                stack.append(((nr, nc), dir, set(list(visited)), score + 1001))

        dr, dc = directions[lrf[2]]
        r += dr
        c += dc
        score += 1

    print(sorted(scores))
