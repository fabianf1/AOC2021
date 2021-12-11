from collections import defaultdict

def load_data(path: str) -> list:
    return [[int(number) for number in list(line)] for line in open(path).read().strip().splitlines()]

def neighbours(i,j, sz_i, sz_j, stack) -> set:
    if i - 1 > -1   and j - 1 > -1  : stack[i-1, j-1] += 1
    if i - 1 > -1                   : stack[i-1, j] += 1
    if i - 1 > -1   and j + 1 < sz_j: stack[i-1, j+1] += 1
    if                  j - 1 > -1  : stack[i, j-1] += 1
    if                  j + 1 < sz_j: stack[i, j+1] += 1
    if i + 1 < sz_i and j - 1 > -1  : stack[i+1, j-1] += 1
    if i + 1 < sz_i                 : stack[i+1, j] += 1
    if i + 1 < sz_i and j + 1 < sz_j: stack[i+1, j+1] += 1
    return stack

def step_octo(d: list[list]) -> int:
    stack = defaultdict(int)
    count = 0
    # Loop 1
    for i in range(len(d)):
        for j in range(len(d[0])):
            d[i][j] += 1
            if d[i][j] > 9:
                stack = neighbours(i, j, len(d), len(d[0]), stack)
                d[i][j] = 0
                count += 1
    # Loop 2
    while len(stack) > 0:
        idx, num = stack.popitem()
        i, j = idx
        if d[i][j] != 0:
            d[i][j] += num
            if d[i][j] > 9:
                stack = stack | neighbours(i, j, len(d), len(d[0]), stack)
                d[i][j] = 0
                count += 1
    return count

def flash_sim(d: list[list], days: int) -> int:
    count = 0

    for n in range(days):
        count+= step_octo(d)
    # Return
    return count

def find_sync_day(d: list[list]) -> int:
    count = 0
    day = 0
    while count != 100:
        count = step_octo(d)
        day += 1
    return day

def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert flash_sim(test, 100) == 1656
    print('Part 1: ' + str(flash_sim(data, 100)))
    # Reload data as list is modified in run above
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 2
    assert find_sync_day(test) == 195
    print('Part 2: ' + str(find_sync_day(data)))

if __name__ == "__main__":
    main()