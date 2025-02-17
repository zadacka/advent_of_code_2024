from collections import defaultdict
import heapq

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

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                sr, sc = r, c

    pq = [(0, sr, sc, 0, 1, [(sr, sc)])]  # cost, r, c, dr, dc, path
    seen = set() #{(sr, sc, 0, 1)}

    paths = defaultdict(set)

    while pq:
        cost, r, c, dr, dc, path = heapq.heappop(pq)
        seen.add((r, c, dr, dc))

        if grid[r][c] == 'E':
            paths[cost].update(set(path))
            # print(cost, len(set(path)))

        for new_cost, nr, nc, ndr, ndc in (
                (cost + 1, r + dr, c + dc, dr, dc),
                (cost + 1000, r , c , dc, -dr),
                (cost + 1000, r , c , -dc, dr),
        ):
            if grid[nr][nc] == '#': continue
            if (nr, nc, ndr, ndc) in seen: continue  # prevent loops
            updated_path = path + [(nr, nc)]
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc, updated_path))

    min_cost = min(paths)
    print(f"{cost}: {len(paths[min_cost])}")