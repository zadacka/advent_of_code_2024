from collections import defaultdict

test_input = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def count_occurrences(input_string):
    rc_to_char = defaultdict(str)
    for row, line in enumerate(input_string.splitlines()):
        for col, char in enumerate(line):
            rc_to_char[(row, col)] = char

    matches = 0
    for r in range(row + 1):
        for c in range(col + 1):
            if rc_to_char[(r, c)] == 'X' and rc_to_char[(r + 1, c)] == "M" and rc_to_char[(r + 2, c)] == 'A' and rc_to_char[(r + 3, c)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'X' and rc_to_char[(r, c + 1)] == "M" and rc_to_char[(r, c + 2)] == 'A' and rc_to_char[(r, c + 3)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'X' and rc_to_char[(r + 1, c + 1)] == "M" and rc_to_char[(r + 2, c + 2)] == 'A' and rc_to_char[(r + 3, c + 3)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'X' and rc_to_char[(r - 1, c + 1)] == "M" and rc_to_char[(r - 2, c + 2)] == 'A' and rc_to_char[(r - 3, c + 3)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r + 1, c)] == "A" and rc_to_char[(r + 2, c)] == 'M' and rc_to_char[(r + 3, c)] == 'X':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r, c + 1)] == "A" and rc_to_char[(r, c + 2)] == 'M' and rc_to_char[(r, c + 3)] == 'X':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r + 1, c + 1)] == "A" and rc_to_char[(r + 2, c + 2)] == 'M' and rc_to_char[(r + 3, c + 3)] == 'X':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r - 1, c + 1)] == "A" and rc_to_char[(r - 2, c + 2)] == 'M' and rc_to_char[(r - 3, c + 3)] == 'X':
                matches += 1
    return matches

def count_cross_occurrences(input_string):
    rc_to_char = defaultdict(str)
    for row, line in enumerate(input_string.splitlines()):
        for col, char in enumerate(line):
            rc_to_char[(row, col)] = char

    matches = 0
    for r in range(row + 1):
        for c in range(col + 1):
            if rc_to_char[(r, c)] == 'M' and rc_to_char[(r + 2, c)] == "S" and rc_to_char[(r +1, c + 1)] == 'A' and rc_to_char[(r, c + 2)] == 'M' and rc_to_char[(r + 2, c + 2)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'M' and rc_to_char[(r + 2, c)] == "M" and rc_to_char[(r +1, c + 1)] == 'A' and rc_to_char[(r, c + 2)] == 'S' and rc_to_char[(r + 2, c + 2)] == 'S':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r + 2, c)] == "S" and rc_to_char[(r +1, c + 1)] == 'A' and rc_to_char[(r, c + 2)] == 'M' and rc_to_char[(r + 2, c + 2)] == 'M':
                matches += 1
            if rc_to_char[(r, c)] == 'S' and rc_to_char[(r + 2, c)] == "M" and rc_to_char[(r +1, c + 1)] == 'A' and rc_to_char[(r, c + 2)] == 'S' and rc_to_char[(r + 2, c + 2)] == 'M':
                matches += 1
    return matches


def test_count_occurrences():
    assert 18 == count_occurrences(test_input)

def test_cross_count_occurrences():
    assert 9 == count_cross_occurrences(test_input)

if __name__ == '__main__':
    day04_input = open("input04.txt").read()
    occurrences = count_occurrences(day04_input)
    print(f"Found: {occurrences} matches of XMAS")

    cross_occurrences = count_cross_occurrences(day04_input)
    print(f"Found: {cross_occurrences} matches of X-MAS")