from collections import deque

from functools import cache

test_input = """\
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def calculate_arrangements(available_towels, target_patterns, find_first=True):
    viable_patterns = 0
    for target_pattern in target_patterns:
        print(f"looking for target pattern {target_pattern}")
        partials = deque([[t] for t in available_towels if target_pattern.startswith(t)])
        while partials:
            partial = partials.popleft()
            # print(partial)
            if ''.join(partial) == target_pattern:
                viable_patterns += 1
                if find_first:
                    break

            for available_towel in available_towels:
                new_partial = partial + [available_towel]
                new_partial_str = ''.join(new_partial)
                if target_pattern.startswith(new_partial_str) and new_partial not in partials:
                    partials.append(new_partial)
    return viable_patterns


if __name__ == '__main__':
    # input_str = test_input
    input_str = open("input19.txt").read()

    towels = [pattern.strip() for pattern in input_str.splitlines()[0].split(',')]
    targets = [target.strip() for target in input_str.splitlines()[2:]]


    @cache
    def can_find(design):
        if design == '': return True
        for i in range(len(design) + 1):
            if design[:i] in towels and can_find(design[i:]):
                return True
        return False


    @cache
    def num_possibilities(design):
        if design == '': return 1
        count = 0
        for i in range(len(design) + 1):
            if design[:i] in towels:
                count += num_possibilities(design[i:])
        return count


    print(sum(can_find(d) for d in targets))
    print(sum(num_possibilities(d) for d in targets))
