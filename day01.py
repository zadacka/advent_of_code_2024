import re

test_input = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


def total_distance(list1, list2):
    return sum(abs(l1 - l2) for l1, l2 in zip(sorted(list1), sorted(list2)))


def test_total_distance():
    list1, list2 = parse_lists(test_input)
    assert 11 == total_distance(list1, list2)


def similarity_score(list1, list2):
    from collections import Counter
    c2 = Counter(list2)
    return sum(i * c2[i] for i in list1)


def test_similarity_score():
    list1, list2 = parse_lists(test_input)
    assert 31 == similarity_score(list1, list2)


def parse_lists(input_string):
    list1, list2 = [], []
    for match in re.findall(r"(\d)\s+(\d)", input_string):
        list1.append(int(match[0]))
        list2.append(int(match[1]))
    return list1, list2


if __name__ == '__main__':
    content = open("input01.txt").read()
    list1, list2 = parse_lists(content)

    total_distance = total_distance(list1, list2)
    print(f"Total Distance: {total_distance}")

    ss = similarity_score(list1, list2)
    print(f"Simliarity Score: {ss}")
