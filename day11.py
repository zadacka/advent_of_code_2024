from collections import Counter

test_input = "0 1 10 99 999"


def permute(stone):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if stone == 0:
        return [1]

    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
    # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on
    # the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    s = str(stone)
    if len(s) % 2 == 0:
        mid = len(s) // 2
        return [int(s[:mid]), int(s[mid:])]

    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024
    # is engraved on the new stone.
    return [stone * 2024]


def blinks(stones):

    result = Counter()
    for stone, count in stones.items():
        new_stones = permute(stone)
        for new_stone in new_stones:
            if new_stone in result:
                result[new_stone] += count
            else:
                result[new_stone] = count
    return result


if __name__ == '__main__':

    # test_stones = [125, 17]
    # stones = Counter(test_stones)
    # for _ in range(26):
    #     stones = blinks(stones)
    #     # print(test_stones)
    #     print(sum(stones.values()))

    # Part 1
    day11_input = open("input11.txt").read()
    stones = Counter([int(i) for i in day11_input.split()])
    for _ in range(75):
        stones = blinks(stones)
    print(sum(stones.values()))


