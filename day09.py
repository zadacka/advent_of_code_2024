test_input = "2333133121414131402"


def decode(input_str):
    from itertools import zip_longest
    result = []
    block_id = 0
    for block_length, gap_length in zip_longest(input_str[::2], input_str[1::2], fillvalue=0):
        result += [str(block_id)] * int(block_length) + ['.'] * int(gap_length)
        block_id += 1
    return result


def reformat(decoded):
    while '.' in decoded:
        first_gap = decoded.index('.')
        decoded[first_gap] = decoded[-1]
        decoded.pop()
        while decoded[-1] == '.':
            decoded.pop()
    return decoded

def reformat2(decoded):
    gaps = []
    blocks = []

    start_idx = 0
    block_id = '0'
    block_length = 0

    for idx, char in enumerate(decoded):
        if char == block_id:
            block_length += 1
        else:
            if block_id == '.':
                gaps.append((start_idx, block_length))
            else:
                blocks.append((start_idx, block_length, block_id))
            start_idx = idx
            block_id = char
            block_length = 1

    blocks.append((start_idx, block_length, block_id))

    for i in range(len(blocks)):
        block_idx, block_len, block_id = blocks[-1-i]
        for j in range(len(gaps)):
            gap_idx, gap_len = gaps[j]
            if gap_idx > block_idx:
                break
            if gap_len >= block_len:
                gaps[j] = (gap_idx + block_len, gap_len - block_len)
                blocks[-1 -i] = (gap_idx, block_len, block_id)
                gaps = [g for g in gaps if g[1] > 0]
                break
    blocks = sorted(blocks, key=lambda x: x[0])
    result = []
    end_idx = 0
    for block in blocks:
        block_idx, block_len, block_id = block
        result += ['.'] * (int(block_idx) - end_idx)
        result += [block_id] * int(block_len)
        end_idx = block_idx + block_len
    return result
def checksum(input_str):
    result = 0
    for idx, block_id in enumerate(input_str):
        if block_id != '.':
            result += idx * int(block_id)
    return result

def part_1():
    # decoded = decode(test_input)
    # print(''.join(decoded))
    # decoded = reformat2(decoded)
    # print(''.join(decoded))
    # result = checksum(decoded)
    # print(result)

    print('real input now....')
    part1_input = open('input09.txt').read().strip()
    decoded = decode(part1_input)
    # print(decoded)
    decoded = reformat2(decoded)
    print(decoded)
    result = checksum(decoded)
    print(result)


def main():
    part_1()


if __name__ == '__main__':
    main()
