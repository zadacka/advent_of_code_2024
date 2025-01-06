# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

# 029A:
# <A^A>^^AvvvA
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

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
    delta_r = end_pos[1] - start_pos[1]
    delta_c = end_pos[0] - start_pos[0]
    result = ""
    result += ">" * delta_r if delta_r > 0 else "<" * (-1 * delta_r)
    result += "^" * delta_c if delta_c > 0 else "v" * (-1 * delta_c)
    return result

def test_first_keypad():
    assert first_keypad('A', '0') == "<"
    assert first_keypad('0', 'A') == "<"

if __name__ == '__main__':
    #  029A: <A^A>^^AvvvA, <A^A^>^AvvvA, and <A^A^^>AvvvA.
    pass

# A -> 0
# 0 -> 2
# 2 -> 9
# 9 -> A
