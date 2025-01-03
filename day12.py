from collections import defaultdict

test_input = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

test_input2 = """\
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""

test_input3 = """\
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

def udlr(pt):
    row, col = pt
    return (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)


if __name__ == '__main__':
    input_to_use = open("input12.txt").read()
    # input_to_use = test_input
    # input_to_use = test_input2
    # input_to_use = test_input3

    row, col = 0, 0
    grid = defaultdict(str)
    for row, line in enumerate(input_to_use.splitlines()):
        for col, char in enumerate(line):
            grid[(row, col)] = char

    unclaimed = dict(grid)
    regions = defaultdict(list)
    region_id = 0
    while unclaimed:
        start_pt, char = list(unclaimed.items())[0]
        perimeter = [start_pt]
        while perimeter:
            pt = perimeter.pop()
            if pt in unclaimed:
                regions[f"{region_id}:{char}"] += [pt]
                unclaimed.pop(pt)
                for next_pt in udlr(pt):
                    if next_pt in unclaimed and unclaimed[next_pt] == char:
                        perimeter.append(next_pt)
        region_id += 1

    areas = {k: len(v) for k, v in regions.items()}
    perimeters = dict()

    for region, pts in regions.items():
        perimeter = 0
        sides = 0
        region_id, char = region.split(':')
        for pt in pts:
            for neighbour in udlr(pt):
                if grid[neighbour] != char:
                    perimeter += 1

        perimeters[region] = perimeter

# part 2 ...........
    range_to_edge = defaultdict(int)
    max_row, max_col = max(grid.keys())
    for region, region_pts in regions.items():
        print(f"region: {region}")
        sides = 0
        range_id, char = region.split(':')

        for row in range(max_row + 1):
            forward_edge_detected = False
            backward_edge_detected = False
            for col in range(max_col + 1):
                pt = (row, col)
                forward_pt = (row + 1, col)
                backward_pt = (row - 1, col)
                if pt in region_pts and grid[forward_pt] != char:
                    if not forward_edge_detected:
                        sides += 1
                        forward_edge_detected = True
                else:
                    forward_edge_detected = False

                if pt in region_pts and grid[backward_pt] != char:
                    if not backward_edge_detected:
                        sides += 1
                        backward_edge_detected = True
                else:
                    backward_edge_detected = False


        for col in range(max_col + 1):
            upward_edge = False
            downward_edge = False
            for row in range(max_row + 1):
                pt = (row, col)
                upward_pt = (row, col - 1)
                downward_pt = (row, col + 1)
                if pt in region_pts and grid[upward_pt] != char:
                    if not upward_edge:
                        sides += 1
                        upward_edge = True
                else:
                    upward_edge = False

                if pt in region_pts and grid[downward_pt] != char:
                    if not downward_edge:
                        sides += 1
                        downward_edge = True
                else:
                    downward_edge = False
        range_to_edge[region] = sides


# /part 2


    fence_cost = 0
    fence_cost2 = 0
    for region, pts in regions.items():
        print(f"{region}: has area {areas[region]}, perimeter {perimeters[region]}, sides {range_to_edge[region]} and pts {pts}")
        fence_cost += areas[region] * perimeters[region]
        fence_cost2 += areas[region] * range_to_edge[region]
    print(f"total fence cost: {fence_cost}, {fence_cost2}")

"""\
.......
.RRRR..
.RRRR..
...RRR.
...R...
"""