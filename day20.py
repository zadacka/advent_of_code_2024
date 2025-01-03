from collections import deque

test_input = """\
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

if __name__ == '__main__':
    # input_str = test_input
    input_str = open("input20.txt").read()

    grid = [list(row) for row in input_str.splitlines()]

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                break  # r, c values preserved
        else:
            continue
        break

    dists = [[-1] * cols for _ in range(rows)]
    q = deque([(r, c)])
    dists[r][c] = 0
    while q:
        r, c = q.popleft()
        for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
            if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
            if dists[nr][nc] != -1: continue  # already better path
            if grid[nr][nc] == '#': continue  # wall
            dists[nr][nc] = dists[r][c] + 1
            q.append((nr, nc))
    # for row in dists:
    #     print(*row, sep='\t')

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#': continue
            for nr, nc in (r + 2, c), (r + 1, c + 1), (r, c + 2), (r - 1, c + 1):
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols: continue
                if grid[nr][nc] == '#': continue
                if abs(dists[r][c] - dists[nr][nc]) >= 102:
                    count += 1
    print(count)
