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

    track = set()
    start = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = r, c
            if grid[r][c] in "SE.":
                track.add((r, c))

    dists = [[-1] * cols for _ in range(rows)]
    q = deque([start])
    r, c = start
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
    for (r, c) in track:
        for (nr, nc) in track:
            shortcut_cost = abs(nr - r) + abs(nc - c)
            saving = dists[nr][nc] - (dists[r][c] + shortcut_cost)
            if shortcut_cost <= 20 and saving >= 100:
                count += 1
    print(count)
