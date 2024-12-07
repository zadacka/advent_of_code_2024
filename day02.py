test_input = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

edge_case = """\
7 10 8 10 11
29 28 27 25 26 25 22 20
"""

def parse_reports(test_input):
    reports = []
    for line in test_input.splitlines():
        reports.append([int(x) for x in line.split()])
    return reports


def is_safe(report, allow_one_bad_level):
    should_increase = report[1] > report[0]
    for idx, a in enumerate(report[:-1]):
        b = report[idx + 1]
        if (
                abs(b - a) > 3 or
                (should_increase and a >= b) or
                (not should_increase and a <= b)
        ):
            # 'not safe' .. but maybe...
            if allow_one_bad_level:
                without_first = [x for x in report]
                del without_first[0]
                without_a = [x for x in report]
                del without_a[idx]
                without_b = [x for x in report]
                del without_b[idx+1]
                if is_safe(without_first, allow_one_bad_level=False):
                    # print(f"***** report {report} becomes 'safe' if we drop first element ... {without_first}")
                    return True
                if is_safe(without_a, allow_one_bad_level=False):
                    # print(f"report {report} becomes 'safe' if we drop {a} ... {without_a}")
                    return True
                elif is_safe(without_b, allow_one_bad_level=False):
                    # print(f"report {report} becomes 'safe' if we drop {b} ... {without_b}")
                    return True
                else:
                    print(f"report {report} cannot be made safe")
                    return False
            return False
    return True


def test_is_safe():
    reports = parse_reports(test_input)
    safe_reports = sum(is_safe(report, allow_one_bad_level=False) for report in reports)
    assert 2 == safe_reports


def test_is_safe_with_tolerance():
    reports = parse_reports(test_input)
    safe_reports = sum(is_safe(report, allow_one_bad_level=True) for report in reports)
    assert 4 == safe_reports

def test_edge_case():
    reports = parse_reports(edge_case)
    safe_reports = sum(is_safe(report, allow_one_bad_level=True) for report in reports)
    assert 2     == safe_reports

if __name__ == '__main__':
    input_string = open("input02.txt").read()
    reports = parse_reports(input_string)
    safe_reports = sum(is_safe(report, allow_one_bad_level=False) for report in reports)
    print(f"There are {safe_reports} safe reports")

    reports = parse_reports(input_string)
    safe_reports_allowing_one_bad_level = sum(is_safe(report, allow_one_bad_level=True) for report in reports)
    print(f"There are {safe_reports_allowing_one_bad_level} safe reports if we allow one bad level")
