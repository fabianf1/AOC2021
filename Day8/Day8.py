from collections import defaultdict
from typing import Tuple

def load_data(path: str) -> list:
    return [[input.split() for input in line.split(' | ')] for line in open(path).read().strip().splitlines()]


def count_unique_numbers_in_output(input: list) -> int:
    count = 0
    for line in input:
        for number in line[1]:
            if len(number) != 5 and len(number) != 6:
                count += 1
    return count


def decode_connections(input: list) -> list:
# seg_map
#     000
#    1   2
#    1   2
#     333
#    4   5
#    4   5
#     666
#
    num_idx = [-1] * 10
    seg_map = [-1] * 7
    # Find indices of 1, 4, 7 and 8
    idx235 = []
    idx069 = []
    for i in range(10):
        if len(input[i]) == 2:
            num_idx[1] = i
        elif len(input[i]) == 4:
            num_idx[4] = i
        elif len(input[i]) == 3:
            num_idx[7] = i
        elif len(input[i]) == 7:
            num_idx[8] = i
        elif len(input[i]) == 5:
            idx235.append(i)
        elif len(input[i]) == 6:
            idx069.append(i)
    # Distinguish 1,3 and 4,6
    char13 = []
    char46 = []
    for char in input[num_idx[8]]:
        if char in input[num_idx[7]]:
            continue
        if char not in input[num_idx[4]]:
            char46.append(char)
        else:
            char13.append(char)
    # Find bottom-left and the number2 using 2,3 and 5
    for idx in idx235:
        if char46[0] in input[idx] and char46[1] in input[idx]:
            num_idx[2] = idx
            idx235.remove(idx)
            if char46[0] not in input[idx235[0]]:
                seg_map[4] = char46[0]
            else:
                seg_map[4] = char46[1]
            break
    # Distinguish top-left and middle, and separate 3 and 5
    for idx in idx235:
        if len(idx235) == 1:
            break
        for char in char13:
            if char not in input[idx]:
                # Number
                num_idx[3] = idx
                idx235.remove(idx)
                num_idx[5] = idx235[0]
                # Mapping
                char13.remove(char)
                seg_map[3] = char13[0]
                break
    # Distinguish 0, 6, 9
    for idx in idx069:
        if seg_map[4] not in input[idx]:
            num_idx[9] = idx
        elif seg_map[3] not in input[idx]:
            num_idx[0] = idx
        else:
            num_idx[6] = idx
    # Found all numbers -> Sort mapping and return
    output = []
    for i in range(10):
        temp = list(input[num_idx[i]])
        temp.sort()
        output.append(temp)

    return output


def sum_output(input: list) -> int:
    count = 0
    for line in input:
        decoder = decode_connections(line[0])
        num = []
        for number in line[1]:
            number = list(number)
            number.sort()
            num.append(decoder.index(number))
        # Number
        count += int(''.join(map(str,num)))

    return count

def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert count_unique_numbers_in_output(test) == 26
    print(count_unique_numbers_in_output(data))
    # Part 2
    assert sum_output(test) == 61229
    print(sum_output(data))


if __name__ == "__main__":
    main()