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
    grid = list([char for char in line] for line in top.splitlines())
    moves = bottom.replace("\n", "")

    rows = len(grid)
    cols = len(grid[0])

    robot = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                robot = (r, c)

    r, c = robot
    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        cr = r
        cc = c
        go = True
        targets = [(r, c)]
        while True:
            cr += dr
            cc += dc
            char = grid[cr][cc]
            if char == '#':
                go = False
                break
            if char == 'O':
                targets.append((cr, cc))
            if char == '.':
                break
        if go:
            grid[r][c] = '.'  # robot moved!
            grid[r + dr][c + dc] = '@'  # robot moved!
            for br, bc in targets[1:]:
                grid[br + dr][bc + dc] = 'O'
            r += dr
            c += dc
    print("---------------")
    for row in grid:
        print(*row, sep='')

    checksum = sum(100 * r + c
                   for r in range(rows)
                   for c in range(cols)
                   if grid[r][c] == 'O'
                   )
    print(checksum)
