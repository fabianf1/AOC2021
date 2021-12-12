def load_data(path: str) -> list:
    return [[x for x in line.split('-')] for line in open(path).read().strip().splitlines()]

def find_connections(d: list) -> dict:
    c = {}
    for x, y in d:
        if y != 'start':
            c1 =  c.get(x, list())
            c1.append(y)
            c.update({x: c1})
        if x != 'start':
            c1 =  c.get(y, list())
            c1.append(x)
            c.update({y: c1})
    return c

def find_num_paths(d: list, double_vist: bool) -> int:
    con_dict = find_connections(d)
    completed_paths = []
    paths = [['start']]
    while len(paths) > 0:
        p = paths.pop()
        for n in con_dict[p[-1]]:
            pc = p.copy()
            pc.append(n)
            if not double_vist and n.islower() and n in p:
                    continue
            elif double_vist and n != 'end' and n.islower():
                if p.count(n) > 1:
                    continue
                elif p.count(n) == 1:
                    entries = [x for x in p if x.islower()]
                    if len(entries) > len(set(entries)):
                        continue
                    elif p.count(n) > 1:
                        continue
            if n == 'end':
                completed_paths.append(pc)
            else:
                paths.append(pc)
    return len(completed_paths)

def main() -> None:
    # Load data
    test = load_data('test.txt')
    test2 = load_data('test2.txt')
    test3 = load_data('test3.txt')
    data = load_data('data.txt')
    # Tests
    assert find_num_paths(test, False) == 10
    assert find_num_paths(test2, False) == 19
    assert find_num_paths(test3, False) == 226
    assert find_num_paths(test, True) == 36
    assert find_num_paths(test2, True) == 103
    assert find_num_paths(test3, True) == 3509
    print('Tests succeeded')
    # Part 1
    print('Part 1: ' + str(find_num_paths(data, False)))
    # Part 2
    print('Part 2: ' + str(find_num_paths(data, True)))


if __name__ == "__main__":
    main()