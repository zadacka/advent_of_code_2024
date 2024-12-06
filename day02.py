test_input = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def parse_reports(test_input):
    for line in test_input.splitlines():
        yield [int(x) for x in line.split()]


def is_safe(report):
    should_increase = report[1] > report[0]
    for a, b in zip(report, report[1:]):
        if (
                abs(b - a) > 3 or
                (should_increase and a >= b) or
                (not should_increase and a <= b)
        ):
            return False
    return True


def test_is_safe():
    reports = list(parse_reports(test_input))
    safe_reports = sum(is_safe(report) for report in reports)
    assert 2 == safe_reports


if __name__ == '__main__':
    input_string = open("input02.txt").read()
    reports = parse_reports(input_string)
    safe_reports = sum(is_safe(report) for report in reports)
    print(f"There are {safe_reports} safe reports")
