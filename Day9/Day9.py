def load_and_prepare_data(path: str) -> list:
    data = [[int(val) for val in list('9' + line + '9')] for line in open(path).read().strip().splitlines()]
    return [[9] * len(data[0])] + data + [[9] * len(data[0])]

def find_min_pos(d: list) -> list:
    min_pos = []
    for i in range(1,len(d)-1):
        for j in range(1,len(d[0])-1):
            if d[i-1][j] > d[i][j] and d[i+1][j] > d[i][j] and d[i][j+1] > d[i][j] and d[i][j-1] > d[i][j]:
                min_pos.append([i,j])
    return min_pos

def calc_risk_sum(d: list) -> int:
    count = 0
    for i, j in find_min_pos(d):
        count += 1 + d[i][j]
    return count

def extend_basin(d:list, i: int, j:int, s: set) -> set:
    if d[i][j] != 9:
        s.add((i,j))
        if (i + 1, j) not in s: s = s | extend_basin(d, i + 1, j, s)
        if (i - 1, j) not in s: s = s | extend_basin(d, i - 1, j, s)
        if (i, j + 1) not in s: s = s | extend_basin(d, i, j + 1, s)
        if (i, j - 1) not in s: s = s | extend_basin(d, i, j - 1, s)
    return s

def basin_size(d: list) ->  int:
    sz_list = []
    for i, j in find_min_pos(d):
        sz_list.append(len(extend_basin(d, i, j, set())))
    sz_list.sort(reverse=True)
    return sz_list[0] * sz_list[1] * sz_list[2]

def main() -> None:
    # Load data
    test = load_and_prepare_data('test.txt')
    data = load_and_prepare_data('data.txt')
    # Part 1
    assert calc_risk_sum(test) == 15
    print('Part 1: ' + str(calc_risk_sum(data)))
    # Part 2
    assert basin_size(test) == 1134
    print('Part 2: ' + str(basin_size(data)))

if __name__ == "__main__":
    main()