from collections import defaultdict

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



def parse_input(input_str):
    grid = defaultdict(str)
    moves = []

    for y, line in enumerate(input_str.splitlines()):
        if line.startswith('#'):
            for x, char in enumerate(line):
                grid[(x, y)] = char
        else:
            for char in line:
                moves.append(char)

    return grid, moves


def print_grid(grid):
    result = ''
    x_max, y_max = max(grid.keys())
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            result += (grid[(x, y)])
        result += '\n'
    return result


def do_move(grid, move):
    max_row, max_col = max(grid.keys())

    robotx, roboty = next((key for key, val in grid.items() if val == '@'), None)
    barrels_to_move = []
    if move == '<':
        for col in range(robotx - 1, 0, -1):
            if grid[col, roboty] == 'O':
                barrels_to_move.append((col, roboty))
            elif grid[col, roboty] == '.':
                for barrel in barrels_to_move:
                    barrelx, barrely = barrel
                    grid[barrelx - 1, barrely] = 'O'
                grid[robotx, roboty] = '.'
                grid[robotx-1, roboty] = '@'
                break
            elif grid[col, roboty] == '#':
                break
    if move == '>':
        for col in range(robotx + 1, max_col):
            if grid[col, roboty] == 'O':
                barrels_to_move.append((col, roboty))
            elif grid[col, roboty] == '.':
                for barrel in barrels_to_move:
                    barrelx, barrely = barrel
                    grid[barrelx + 1, barrely] = 'O'
                grid[robotx, roboty] = '.'
                grid[robotx+1, roboty] = '@'
                break
    if move == '^':
        for row in range(roboty - 1, 0, -1):
            item = grid[robotx, row]
            if item == 'O':
                barrels_to_move.append((robotx, row))
            elif item == '.':
                for barrel in barrels_to_move:
                    barrelx, barrely = barrel
                    grid[barrelx, barrely - 1] = 'O'
                grid[robotx, roboty] = '.'
                grid[robotx, roboty - 1] = '@'
                break
            else:
                break # probably hit the edge
    if move == 'v':
        for row in range(roboty + 1, max_row):
            item = grid[robotx, row]
            if item == 'O':
                barrels_to_move.append((robotx, row))
            elif item == '.':
                for barrel in barrels_to_move:
                    barrelx, barrely = barrel
                    grid[barrelx, barrely + 1] = 'O'
                grid[robotx, roboty] = '.'
                grid[robotx, roboty + 1] = '@'
                break
            else:
                break # probably hit the edge
    return grid


def calculate_checksum(grid):
    result = 0
    for pt, value in grid.items():
        if value == 'O':
            x,y = pt
            result += 100 * y + x
    return result


if __name__ == '__main__':
    gridmap, moves = parse_input(open("input15.txt").read())


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

            gridmap = do_move(gridmap, move)
            result = ""
            for row in grid:
                result += ''.join(row) + '\n'
            result2 = print_grid(gridmap)
            if result != result2:
                print(f"MISMATCH ALREADY!!!")
                print("---------------")
                print(result)
                print("---------------")
                print(result2)



    print(f"Finally")
    result = ""
    for row in grid:
        result += ''.join(row) + '\n'
    result2 = print_grid(gridmap)
    print("---------------")
    print(result)
    print("---------------")
    print(result2)

    print(f"My checksum: {calculate_checksum(gridmap)}")
    checksum = sum(100 * r + c
                   for r in range(rows)
                   for c in range(cols)
                   if grid[r][c] == 'O'
                   )
    print(f"Other checksum: {checksum}")