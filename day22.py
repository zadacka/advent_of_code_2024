from collections import deque, defaultdict


def mix(a, b):
    """ Bitwise XOR"""
    return a ^ b


def test_mix():
    assert 37 == mix(42, 15)


def prune(a):
    return a % 16777216


def advance(a):
    a = prune(mix(a, a * 64))
    a = prune(mix(a, a // 32))
    a = prune(mix(a, a * 2048))
    return a


def test_advance():
    sequence = [123, 15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254]
    for first, second in zip(sequence, sequence[1:]):
        assert second == advance(first)


def test_prune():
    assert 16113920 == prune(100000000)


def test_part1_test():
    secrets = [1, 10, 100, 2024]
    expected_two_thousands = [8685429, 4700978, 15273692, 8667524]
    results = []
    for secret_number in secrets:
        for _ in range(2000):
            secret_number = advance(secret_number)
        print(secret_number)
        results.append(secret_number)
    assert results == expected_two_thousands


def part1():
    secrets = [int(i) for i in open("input22.txt").read().splitlines()]
    results = []
    for progress, secret_number in enumerate(secrets):
        if progress % 50 == 0:
            print(f"Progress: {progress}/{len(secrets)}")
        for _ in range(2000):
            secret_number = advance(secret_number)
        results.append(secret_number)
    print(sum(results))


def test_part2_test():
    secrets = [1, 2, 3, 2024]
    best_pattern = get_most_bananas(secrets)
    assert best_pattern == {(-2, 1, -1, 3): 23}


def part2():
    secrets = [int(l) for l in open("input22.txt").read().splitlines()]
    best_pattern = get_most_bananas(secrets)
    print(best_pattern)


def get_most_bananas(secrets):
    all_patterns = defaultdict(int)
    for secret_number in secrets:
        patterns = dict()
        window = deque(maxlen=4)
        for _ in range(2000):
            previous_number = secret_number
            secret_number = advance(secret_number)
            diff = int(str(secret_number)[-1]) - int(str(previous_number)[-1])
            window.append(diff)
            if len(window) == 4:
                if tuple(window) not in patterns:
                    patterns[tuple(window)] = int(str(secret_number)[-1])
        for pattern, value in patterns.items():
            all_patterns[pattern] += value
    max_value = max(all_patterns.values())
    best_pattern = {k: v for k, v in all_patterns.items() if v == max_value}
    return best_pattern
