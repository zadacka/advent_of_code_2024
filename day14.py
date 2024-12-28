import dataclasses

import math

import re

test_input = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

# test_input = """\
# p=2,4 v=2,-3"""
@dataclasses.dataclass
class Robot:
    x:int
    y:int
    vx:int
    vy:int

# BOARD_WIDTH = 11
BOARD_WIDTH = 101
BOARD_HEIGHT = 103
# BOARD_HEIGHT = 7


def print_board(robots):
    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if any(robot.y == r and robot.x == c for robot in robots):
                print('x', end='')
            else:
                print('.', end='')
        print('')


if __name__ == '__main__':
    input_string = test_input
    input_string = open("input14.txt").read()

    robots = []
    for line in input_string.splitlines():
        match = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        robots.append(
            Robot(int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)))
        )
    print(robots)
    seconds_left = 100
    while seconds_left:
        # print_board(robots)

        for robot in robots:
            # print(f"Current point: {robot.x}, {robot.y}, moving {robot.vx}, {robot.vy}")
            robot.x += robot.vx
            robot.y += robot.vy
            if robot.x > 0:
                robot.x = robot.x % BOARD_WIDTH
            while robot.x < 0:
                robot.x += BOARD_WIDTH
            if robot.y > 0:
                robot.y = robot.y % BOARD_HEIGHT
            while robot.y < 0:
                robot.y += BOARD_HEIGHT
            # print(f"-> to {robot.x}, {robot.y}")
        seconds_left -= 1

    quadrants = [0,0,0,0]
    # for r in range(BOARD_HEIGHT):
    #     for c in range(BOARD_WIDTH):
    for robot in robots:
        if robot.y < BOARD_HEIGHT // 2:
            if robot.x < BOARD_WIDTH // 2:
                quadrants[0] += 1
            elif robot.x > BOARD_WIDTH // 2:
                quadrants[1] += 1
        elif robot.y > BOARD_HEIGHT // 2:
            if robot.x < BOARD_WIDTH // 2:
                quadrants[2] += 1
            elif robot.x > BOARD_WIDTH // 2:
                quadrants[3] += 1
    print(quadrants)
    print(math.prod(quadrants))