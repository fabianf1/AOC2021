def load_data(path: str):
    tpl, _, *rules = open(path).read().strip().split('\n')
    rules = dict(r.split(" -> ") for r in rules)
    return [tpl, rules]

def get_common_diff(tpl: str, rules: dict, steps: int) -> int:
    pairs = {}
    chars = {}
    for j in range(len(tpl)):
        chars[tpl[j]] = chars.get(tpl[j], 0) + 1
        if j+1 < len(tpl):
            pairs[tpl[j:j + 2]] = pairs.get(tpl[j:j + 2], 0) + 1
    for i in range(steps):
        for (a,b), c in pairs.copy().items():
            x = rules[a+b]
            pairs[a+b] -= c
            pairs[a+x] = pairs.get(a+x, 0) + c
            pairs[x+b] = pairs.get(x+b, 0) + c
            chars[x] = chars.get(x, 0) + c
    return max(chars.values()) - min(chars.values())

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