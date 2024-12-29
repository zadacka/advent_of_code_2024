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
    forward_left_right = {'N': 'NWE', 'S': 'SWE', 'E': 'ENS', 'W': 'WNS'}
    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}
    stack = [(start, 'E', [], 0), ]  # position, direction, visited, score

    del c, char, r, input_str, test_input,

    scores = []

    while stack:
        position, direction, visited, score = stack.pop()
        r, c = position
        if gridmap[position] == 'E':
            print(f"Made it! {score}")
            scores.append(score)
            continue

        path_so_far = set(visited)
        path_so_far.add(position)

        for new_direction in list(forward_left_right[direction]):
            dr, dc = directions[new_direction]
            nr, nc = r + dr, c + dc
            score_modifier = 1 if new_direction == direction else 1001
            if gridmap[(nr, nc)] in ['.', 'E'] and (nr, nc) not in visited:
                stack.append(
                    ((nr, nc), new_direction, path_so_far, score + score_modifier)
                )
    print(sorted(scores))
