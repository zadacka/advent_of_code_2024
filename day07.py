from collections import deque

import itertools

test_input = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def parse_input(test_input):
    result = []
    for line in test_input.splitlines():
        target, terms = line.split(':')
        terms = terms.split()
        result.append([int(target), [int(t) for t in terms]])
    return result


def test_parse_input():
    expected = [
        [190, [10, 19]],
        [3267, [81, 40, 27]],
        [83, [17, 5]],
        [156, [15, 6]],
        [7290, [6, 8, 6, 15]],
        [161011, [16, 10, 13]],
        [192, [17, 8, 14]],
        [21037, [9, 7, 18, 13]],
        [292, [11, 6, 16, 20]]
    ]
    assert expected == parse_input(test_input)


def is_valid(target, terms):
    gaps = len(terms) - 1

    for multiply_operators in range(gaps + 1):
        addition_operators = gaps - multiply_operators
        operator_combos = '*' * multiply_operators + '+' * addition_operators
        results = []
        for permutation in set(itertools.permutations(operator_combos)):
            term_stack = deque([t for t in terms])
            result = 0
            for operator in permutation:
                first = term_stack.popleft()
                second = term_stack.popleft()
                result = first + second if operator == '+' else first * second
                term_stack.appendleft(result)
            if result == target:
                return True
            results.append(result)
        if all(result > target for result in results):
            return False  # no point adding more multiply gaps, we're always over the target already!
    return False


def test_valid():

    assert is_valid(190, [10, 19])
    assert is_valid(3267, [81, 40, 27])
    assert not is_valid(83, [17, 5])
    assert not is_valid(156, [15, 6])
    assert not is_valid(7290, [6, 8, 6, 15])
    assert not is_valid(161011, [16, 10, 13])
    assert not is_valid(192, [17, 8, 14])
    assert not is_valid(21037, [9, 7, 18, 13])
    assert is_valid(292, [11, 6, 16, 20])

def main():
    input_str = open('input07.txt').read()
    parsed_input = parse_input(input_str)
    result = 0
    for target, terms in parsed_input:
        if is_valid(target, terms):
            result += target
    print(f"The total of valid lines is: {result}")

if __name__ == '__main__':
    main()