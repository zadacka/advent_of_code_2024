test_input = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def input_to_rules_and_updates(input_string):
    rules, updates = input_string.split('\n\n')
    from collections import defaultdict
    rulemap = defaultdict(set)
    for rule in rules.split():
        before, after = rule.split('|')
        rulemap[int(before)].add(int(after))

    update_list = []
    for update in updates.split():
        update_list.append([int(page) for page in update.split(',')])

    print(rulemap, update_list)
    return rulemap, update_list


def test_input_to_rules_and_updates():
    rulemap, updates = input_to_rules_and_updates(test_input)
    assert rulemap == {
        29: {13},
        47: {29, 13, 61, 53},
        53: {13, 29},
        61: {29, 53, 13},
        75: {13, 47, 29, 53, 61},
        97: {75, 13, 47, 61, 53, 29}
    }
    assert updates == [
        [75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29],
        [97, 13, 75, 29, 47]]


def is_valid(update, rulemap):
    already_seen = set()
    for page in update:
        must_come_after = rulemap[page]
        if must_come_after.intersection(already_seen):
            return False
        already_seen.add(page)
    return True


def test_is_valid():
    valid = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13]]
    invalid = [[75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]
    from collections import defaultdict
    rulemap = defaultdict(set, {
        29: {13},
        47: {29, 13, 61, 53},
        53: {13, 29},
        61: {29, 53, 13},
        75: {13, 47, 29, 53, 61},
        97: {75, 13, 47, 61, 53, 29}
    })
    for update in valid:
        assert is_valid(update, rulemap)

    for update in invalid:
        assert not is_valid(update, rulemap)


def test_part1():
    rulemap, updates = input_to_rules_and_updates(test_input)
    assert 143 == calculate_mid(updates, rulemap)


def test_part2():
    rulemap, updates = input_to_rules_and_updates(test_input)
    assert 123 == calculate_mid(updates, rulemap, calculate_valid=False)


def calculate_mid(updates, rulemap, calculate_valid=True):
    total = 0
    for update in updates:
        mid_idx = len(update) // 2
        valid = is_valid(update, rulemap)
        if valid and calculate_valid:
            total += update[mid_idx]
        elif not valid and not calculate_valid:
            reordered = reorder(update, rulemap)
            total += reordered[mid_idx]
        else:
            pass
    return total


def reorder(update, rulemap):
    while not is_valid(update, rulemap):
        already_seen = set()
        for idx, page in enumerate(update):
            must_come_after = rulemap[page]
            intersection = must_come_after.intersection(already_seen)
            already_seen.add(page)
            if intersection:
                page_to_reorder = intersection.pop()
                idx2 = update.index(page_to_reorder)
                update[idx] = page_to_reorder
                update[idx2] = page
                break
    return update


def test_reorder():
    invalid = [[75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]
    from collections import defaultdict
    rulemap = defaultdict(set, {
        29: {13},
        47: {29, 13, 61, 53},
        53: {13, 29},
        61: {29, 53, 13},
        75: {13, 47, 29, 53, 61},
        97: {75, 13, 47, 61, 53, 29}
    })

    assert [97, 75, 47, 61, 53] == reorder(invalid[0], rulemap)
    assert [61, 29, 13] == reorder(invalid[1], rulemap)
    assert [97, 75, 47, 29, 13] == reorder(invalid[2], rulemap)


def main():
    input_str = open("input05.txt").read()
    rulemap, updates = input_to_rules_and_updates(input_str)
    mid = calculate_mid(updates, rulemap)
    print(f"Mid value for part 1 is {mid}")
    invalid_mid = calculate_mid(updates, rulemap, calculate_valid=False)
    print(f"Mid value for part 1 is {invalid_mid}")


if __name__ == '__main__':
    main()
