# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

# input line 379A requires keypad1       ^A              ^^  <<     A              >>AvvvA
# ... and that requires requires keypad2 <A>A           <AA,v<AA,>>^A      vAA^Av<AAA>^A
# ... and that requires requires keypad3 v<<A>>^AvA^A   v<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A
# or.....................................<v<A>>^AvA^A   <vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
def first_keypad(start, end):
    key_positions = {
        'A': (3, 2),
        '0': (3, 1),
        '1': (2, 0),
        '2': (2, 1),
        '3': (2, 2),
        '4': (1, 0),
        '5': (1, 1),
        '6': (1, 2),
        '7': (0, 0),
        '8': (0, 1),
        '9': (0, 2),
    }
    start_pos = key_positions[start]
    end_pos = key_positions[end]
    delta_r = end_pos[0] - start_pos[0]
    delta_c = end_pos[1] - start_pos[1]
    result = ""
    if delta_c > 0: result += ">" * delta_c
    if delta_r < 0: result += "^" * (-1 * delta_r)
    if delta_r > 0: result += "v" * delta_r
    if delta_c < 0: result += "<" * (-1 * delta_c)
    return result + 'A'


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
def second_keypad(start, end):
    key_positions = {
        'A': (0, 2),
        '^': (0, 1),
        'v': (1, 1),
        '<': (1, 0),
        '>': (1, 2),
    }
    start_pos = key_positions[start]
    end_pos = key_positions[end]
    delta_r = end_pos[0] - start_pos[0]
    delta_c = end_pos[1] - start_pos[1]
    result = ""
    # order is important to avoid the empty keypad: go right before up, go down before left
    if delta_c > 0: result += ">" * delta_c
    if delta_r < 0: result += "^" * (-1 * delta_r)
    if delta_r > 0: result += "v" * delta_r
    if delta_c < 0: result += "<" * (-1 * delta_c)
    return result + 'A'


def test_first_keypad():
    assert first_keypad('A', '0') == "<A"
    assert first_keypad('0', '2') == "^A"
    assert first_keypad('2', '9') == ">^^A"
    assert first_keypad('9', 'A') == "vvvA"


def test_second_keypad():
    two_zero_nine_a = "<A^A>^^AvvvA"
    result = "".join(second_keypad(start, end) for start, end in zip("A" + two_zero_nine_a, two_zero_nine_a))
    assert len(result) == len("v<<A>>^A<A>AvA<^AA>A<vAAA>^A")


def test_third_keypad():
    stuff = "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"
    result = "".join(second_keypad(start, end) for start, end in zip("A" + stuff, stuff))
    assert len(result) == len("<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A")
    # 029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
    # 980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
    # 179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
    # 456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
    # 379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A


test_input = """\
029A
980A
179A
456A
379A"""


def calculate_complexities(input_str):
    input_cmds = input_str.splitlines()
    total = 0
    for input_line in input_cmds:
        result = ""
        for first, second in zip('A' + input_line, input_line):
            result += first_keypad(first, second)
        print(f"input line {input_line} requires keypad1 {result}")

        result2 = ""
        for first, second in zip('A' + result, result):
            result2 += second_keypad(first, second)
        print(f"... and that requires requires keypad2 {result2}")

        result3 = ""
        for first, second in zip('A' + result2, result2):
            result3 += second_keypad(first, second)
        print(f"... and that requires requires keypad3 {result3}")
        button_presses = len(result3)
        numeric_part = int(input_line[:-1])
        print(f"with a score of {button_presses} * {numeric_part}")
        total += button_presses * numeric_part
    print(f"total score: {total}")
    return total


def test_lines():
    for input_line, expected in (
            ("029A", "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"),
            ("980A", "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A"),
            ("179A", "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"),
            ("456A", "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A"),
            ("379A", "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")):
        result = ""
        for first, second in zip('A' + input_line, input_line):
            result += first_keypad(first, second)
        print(f"input line {input_line} requires keypad1 {result}")

        result2 = ""
        for first, second in zip('A' + result, result):
            result2 += second_keypad(first, second)
        print(f"... and that requires requires keypad2 {result2}")

        result3 = ""
        for first, second in zip('A' + result2, result2):
            result3 += second_keypad(first, second)
        print(f"... and that requires requires keypad3 {result3}")
        print(f"*** with length {len(result3)} ****")
        wrong = 'v<<A>>^AvA^Av<<A>>^AAv<A<A>>^AAvAA^<A>Av<A>^AA<A>Av<A<A>>^AAAvA^<A>A'
        correct = '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
        assert len(result3) == len(expected)


#  68 * 29, 60 * 980, 68 * 179, 64 * 456, and 64 * 379
def test_part1():
    # input_str = test_input
    # input_str = open("input21.txt").read()
    assert 123 == calculate_complexities(test_input)


# v<<A>>^A<A>AvA<^AA>A<vAAA>^A
# v<<A>>^A<A>AvA^<AA>Av<AAA>^A
# v<A<AA>>^AvAA^<A>Av<<A>>^AvA^Av<A>^A<Av<A>>^AAvA^Av<A<A>>^AAAvA^<A>A
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

def test_manual():
    one = "^^<<"
    result = "".join(second_keypad(first, second) for first, second in zip('A'+ one, one))
    assert result == '<AAv<AA'

    two = "^<^<"
    result = "".join(second_keypad(first, second) for first, second in zip('A'+ two, two))
    assert result == '<Av<A>^Av<A'

    three = "<<^^"
    result = "".join(second_keypad(first, second) for first, second in zip('A'+ three, three))
    assert result == 'v<<AA>^AA'

    four = "^^<<"
    result = "".join(second_keypad(first, second) for first, second in zip('A'+ four, four))
    assert result == '<AAv<AA'

if __name__ == '__main__':
    pass
