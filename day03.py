import re

test_input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_input_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def calculate(corrupted_string):
    return sum(int(match[0]) * int(match[1]) for match in re.findall(r"mul\((\d+),(\d+)\)", corrupted_string))


def test_calculate():
    assert 161 == calculate(test_input)


def get_valid_input(corrupted_input):
    if "don't()" not in corrupted_input:
        return corrupted_input

    corrupted_input = ''.join(corrupted_input.splitlines())   # make all one line so we don't have issues with ^ and $

    result = ""
    first_match = re.match(r"^(.*?)(?:do\(\)|don't\(\))", corrupted_input)  # start to the first do() or don't()
    result += first_match[1]

    other_matches = re.findall(r"do\(\)(.*?)don't\(\)", corrupted_input)  # do() to don't() bits in the middle
    for match in other_matches:  # single capture group so result should be a list of strings
        result += match

    last_match = re.match(r".*do\(\)(?!.*don't)(.*)$", corrupted_input)  # last do() (not followed by a don't) to the end
    if last_match:
        result += last_match[1]

    return result


def test_calculate_valid_sections():
    valid_sections = get_valid_input(test_input_2)
    assert 48 == calculate(valid_sections)


if __name__ == '__main__':
    day03_input = open("input03.txt").read()
    product = calculate(day03_input)
    print(f"The product of valid instructions is {product}")

    filtered_input = get_valid_input(day03_input)
    part2_product = calculate(filtered_input)
    print(f"The part2 product of valid instructions is {part2_product}")
