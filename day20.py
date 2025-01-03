from collections import deque, defaultdict

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
    input_str = test_input
    input_str = open("input20.txt").read()

    grid = [list(row) for row in input_str.split('\n')]
    start = None
    end = None
    track = set()
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == 'S':
                start = (r, c)
            elif char == 'E':
                end = (r, c)
            if char in 'S.E':
                track.add((r, c))

    seen = {start: 0}
    q = deque([(*start, 0)])
    full_path = None

    while q:
        r, c, d = q.popleft()
        # print(r, c)
        if (r, c) == end:
            print(f"best path: {d}")
            full_path = d
            break
        for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
            if (nr, nc) in track and (nr, nc) not in seen:
                q.append((nr, nc, d + 1))
                seen[(nr, nc)] = d + 1

    distance_from_end = {k: d - v for k, v in seen.items()}

    pts = track - set(distance_from_end.keys())
    for tr, tc in pts:
        if (tr, tc) in distance_from_end:
            continue

        q = deque([(tr, tc, 0)])
        seen2 = {(tr, tc): 0}
        while q:
            r, c, d = q.popleft()
            if (r, c) in distance_from_end:
                for pt, d in seen2.items():
                    distance_from_end[pt] = d + distance_from_end[(r, c)]
            for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
                if (nr, nc) in track and (nr, nc) not in seen:
                    q.append((nr, nc, d + 1))
                    seen2[(nr, nc)] = d + 1
    print(distance_from_end)

    saved = defaultdict(int)
    for (r, c), distance in seen.items():
        for nr, nc in (r + 2, c), (r - 2, c), (r, c - 2), (r, c + 2):
            if (nr, nc) in track:
                new_path_time = distance + distance_from_end[(nr, nc)] + 2
                if new_path_time < full_path:
                    saved[full_path - new_path_time] += 1
                    # print(f"Found a short cut!")
    for k in sorted(saved):
        print(f"Found {saved[k]} paths that saved {k} picoseconds")

    great_cheats = 0
    for k, v in saved.items():
        if v > 100:
            great_cheats += k

    print(f"Great cheats: {great_cheats}")
