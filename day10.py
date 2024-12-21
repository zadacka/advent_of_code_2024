test_input = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

from collections import deque, defaultdict

from dataclasses import dataclass


@dataclass
class Point:
    row: int
    col: int
    height: int
    path: list

    @property
    def left(self):
        return self.row - 1, self.col

    @property
    def right(self):
        return self.row + 1, self.col

    @property
    def up(self):
        return self.row, self.col - 1

    @property
    def down(self):
        return self.row, self.col + 1


def get_map_and_trailheads(input_str):
    rc2height = {}
    trailheads = deque()
    for r, line in enumerate(input_str.splitlines()):
        for c, height in enumerate(line):
            pt = Point(r, c, int(height), path=[(r, c, int(height))])
            rc2height[(r, c)] = pt
            if pt.height == 0:
                trailheads.append(pt)
    return rc2height, trailheads


def get_scores(rc2height, trailheads):
    rating = 0
    base2peaks = defaultdict(set)
    while trailheads:
        trailhead = trailheads.popleft()
        if trailhead.height == 9:
            base2peaks[trailhead.path[0]].add((trailhead.row, trailhead.col))
            rating += 1

        for direction in trailhead.left, trailhead.right, trailhead.up, trailhead.down:
            height = rc2height[direction].height if direction in rc2height else -1
            if height == trailhead.height + 1:
                trailheads.appendleft(Point(*direction, height=height, path=trailhead.path + [(*direction, height)]))
    return {k:len(v) for k, v in base2peaks.items()}, rating


if __name__ == '__main__':
    rc2height, trailheads = get_map_and_trailheads(test_input)
    scores, rating = get_scores(rc2height, trailheads)
    print(sum(scores.values()), rating)

    part1_input = open("input10.txt").read()
    rc2height, trailheads = get_map_and_trailheads(part1_input)
    scores, rating = get_scores(rc2height, trailheads)
    print(sum(scores.values()), rating)