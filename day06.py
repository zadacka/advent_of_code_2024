import copy

puzzle_input = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def parse(input_string):
    start_position = None
    from collections import defaultdict
    grid = defaultdict(str)

    for row, line in enumerate(puzzle_input.split()):
        for col, char in enumerate(line):
            grid[(row, col)] = char
            if char == '^':
                start_position = (row, col)
                grid[(row, col)] = '.'
    return start_position, grid


def move(current_position, current_direction, grid):
    if current_direction == 'UP':
        up = (current_position[0] - 1, current_position[1])
        return (current_position, 'RIGHT') if grid[up] == '#' else (up, 'UP')
    elif current_direction == 'DOWN':
        down = (current_position[0] + 1, current_position[1])
        return (current_position, 'LEFT') if grid[down] == '#' else (down, 'DOWN')
    elif current_direction == 'RIGHT':
        right = (current_position[0], current_position[1] + 1)
        return (current_position, 'DOWN') if grid[right] == '#' else (right, 'RIGHT')
    elif current_direction == 'LEFT':
        left = (current_position[0], current_position[1] - 1)
        return (current_position, 'UP') if grid[left] == '#' else (left, 'LEFT')
    else:
        raise RuntimeError(f'Invalid direction: {current_direction}')


def test_count_moves():
    current_position, grid = parse(puzzle_input)
    start_position = current_position
    current_direction = 'UP'
    visited_positions = {tuple(current_position), }
    while True:
        current_position, current_direction = move(current_position, current_direction, grid)
        if grid[current_position] == '':
            break
        visited_positions.add(tuple(current_position))
    assert 41 == len(visited_positions)

    loops = 0
    for candidate_obstacle in visited_positions:
        new_grid = copy.deepcopy(grid)
        new_grid[candidate_obstacle] = '#'
        if candidate_obstacle == start_position:
            continue

        from collections import defaultdict
        this_route = defaultdict(list)
        current_position = start_position
        current_direction = 'UP'
        while True:
            current_position, current_direction = move(current_position, current_direction, new_grid)
            if new_grid[current_position] == '':
                break
            if current_direction in this_route[current_position]:
                loops += 1
                break
            this_route[current_position].append(current_direction)
    assert loops == 6




if __name__ == '__main__':
    puzzle_input = open('input06.txt').read()
    start_position, grid = parse(puzzle_input)
    current_position = start_position
    current_direction = 'UP'
    visited_positions = {tuple(current_position), }
    while True:
        current_position, current_direction = move(current_position, current_direction, grid)
        if grid[current_position] == '':
            break
        visited_positions.add(tuple(current_position))
    print(f"There were {len(visited_positions)} valid moves.")

    loops = 0
    candidate = 0
    for candidate_obstacle in visited_positions:
        print(f"{candidate}/{len(visited_positions)}")
        candidate += 1
        new_grid = copy.deepcopy(grid)
        new_grid[candidate_obstacle] = '#'
        if candidate_obstacle == start_position:
            continue

        from collections import defaultdict
        this_route = defaultdict(list)
        current_position = start_position
        current_direction = 'UP'
        while True:
            current_position, current_direction = move(current_position, current_direction, new_grid)
            if new_grid[current_position] == '':
                break
            if current_direction in this_route[current_position]:
                loops += 1
                break
            this_route[current_position].append(current_direction)
    print(f"Loops: {loops}")

#  to interact with the guard, an obstacle must be placed on the route
#  (other than the starting place)

# for each possible obstacle...
# extend the 'seen before' map to include direction!
# keep moving until one of two end conditions:
# 'seen before' is encountered again with with the same direction OR we have left the map

