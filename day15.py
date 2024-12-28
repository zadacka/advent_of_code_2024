small_example = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

test_input = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

if __name__ == '__main__':
    # input_str = test_input
    input_str = open("input15.txt").read()

    top, bottom = input_str.split('\n\n')
    expansion = {'#': '##', '.': '..', 'O': '[]', '@': '@.'}
    grid = [
        list(''.join([expansion[char] for char in line]))
        for line in top.splitlines()
    ]
    # for row in grid:
    #     print(''.join(row))
    moves = bottom.replace("\n", "")

    rows = len(grid)
    cols = len(grid[0])

    robot = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                robot = (r, c)

    r, c = robot
    # print(f"robot at {robot}")
    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        go = True
        targets = [(r, c)]
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in targets: continue  # already added this, don't need to check again
            char = grid[nr][nc]
            if char == '#':
                go = False
                break
            if char == '[':
                targets.append((nr, nc))
                targets.append((nr, nc + 1))
            if char == ']':
                targets.append((nr, nc - 1))
                targets.append((nr, nc))
        if go:
            copy = [list(row) for row in grid]  # since we will modify it live
            grid[r][c] = '.'
            grid[r + dr][c + dc] = '@'
            for br, bc in targets[1:]:
                grid[br][bc] = '.'
            for br, bc in targets[1:]:
                grid[br + dr][bc + dc] = copy[br][bc]
            r += dr
            c += dc

    checksum = sum(100 * r + c
                   for r in range(rows)
                   for c in range(cols)
                   if grid[r][c] == '['
                   )
    print(checksum)
