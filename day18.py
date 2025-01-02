from collections import deque

test_input = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


def l2rc(l):
    x, y = l.split(',')
    return int(y), int(x)  # row, col


def find_shortest_path(corrupt_blocks):
    GRID_SIZE = 70  # max(max(point) for point in corrupt_blocks)
    search_perimeter = deque()
    for r1, c1 in (1, 0), (0, 1):
        if (r1, c1) not in corrupt_blocks:
            search_perimeter.append((1, 0))
    seen = {(0, 0): 0}

    shortest_path = None
    while search_perimeter:
        row, col = search_perimeter.popleft()

        best_path_neighbour = []
        for nr, nc in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
            if nr < 0 or nc < 0 or nr > GRID_SIZE or nc > GRID_SIZE:
                continue
            elif (nr, nc) in corrupt_blocks:
                continue
            elif (nr, nc) in seen:
                best_path_neighbour.append(seen[(nr, nc)])
            elif (nr, nc) not in search_perimeter:
                search_perimeter.append((nr, nc))
            else:
                pass
        best_path_score = min(best_path_neighbour) + 1
        seen[(row, col)] = best_path_score
        if row == GRID_SIZE and col == GRID_SIZE:
            shortest_path = best_path_score
            break
    return shortest_path


if __name__ == '__main__':

    # input_str = test_input
    input_str = open("input18.txt").read()

    corrupt_blocks = [l2rc(line) for line in input_str.splitlines()]

    for block_limit in range(len(corrupt_blocks)):
        blocks = set(corrupt_blocks[:block_limit])
        path = find_shortest_path(blocks)
        if path is None:
            print(block_limit)
            print(corrupt_blocks[block_limit])
            print(corrupt_blocks[block_limit-1])  #<---- this is actually the answer
            break
        print(path)

    # for row in range(GRID_SIZE):
    #     for col in range(GRID_SIZE):
    #         if (row, col) in corrupt_blocks:
    #             print('#', end='')
    #         elif (row, col) in seen:
    #             print(seen[row, col], end=''),
    #         else:
    #             print('.', end='')
    #     print('')
