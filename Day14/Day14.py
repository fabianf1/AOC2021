def load_data(path: str):
    data = open(path).read().strip().split('\n\n')

    pair = []
    addition = []
    for d in data[1].splitlines():
        d = d.split(' -> ')
        pair.append(d[0])
        addition.append(d[1])

    return [data[0], [pair, addition]]

def get_common_diff(t: str, rules: list, steps: int) -> int:
    pairs = {}
    chars = {}
    for j in range(len(t)):
        chars[t[j]] = chars.get(t[j], 0) + 1
        if j+1 < len(t):
            pair = t[j:j+2]
            pairs[pair] = pairs.get(pair, 0) + 1
    #
    for i in range(steps):
        pairs_o = pairs.copy()
        for key in pairs_o:
            num = pairs_o[key]
            add = rules[1][rules[0].index(key)]

            pairs[key] -= num

            pair1 = key[0] + add
            pair2 = add + key[1]
            pairs[pair1] = pairs.get(pair1, 0) + num
            pairs[pair2] = pairs.get(pair2, 0) + num

            chars[add] = chars.get(add, 0) + num
    #
    val = [chars[key] for key in chars]
    return max(val) - min(val)

def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert get_common_diff(*test, 10) == 1588
    print('Part 1: ' + str(get_common_diff(*data, 10)))
    # Part 2
    assert get_common_diff(*test, 40) == 2188189693529
    print('Part 2: ' + str(get_common_diff(*data, 40)))

if __name__ == "__main__":
    main()