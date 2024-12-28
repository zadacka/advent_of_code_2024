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
    print(result)


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
    # grid, moves = parse_input(small_example)
    grid, moves = parse_input(test_input)
    # grid, moves = parse_input(open("input15.txt").read())

    # print(f"Initial state:")
    # print_grid(grid)

    for move in moves:
        grid = do_move(grid, move)
        # print(f"Move {move}:")
        # print_grid(grid)

    checksum = calculate_checksum(grid)
    print(f"Checksum: {checksum}")

    # smaller: 2028
    # medium: 10092.
