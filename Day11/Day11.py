def load_data(path: str) -> dict:
    # Dictionary sort of works like a 2D array
    return  {(x, y): int(e) for x, l in enumerate(open(path))
                            for y, e in enumerate(l.strip())}

def neighbours(i: int, j: int, d: dict) -> filter:
    # If none or 0: Position is not used
    return filter(d.get, [(i + 1, j + 1), (i + 1, j), (i + 1, j - 1), (i, j + 1),
                          (i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1)])

def step_octo(d: dict) -> int:
    count = 0
    # Increment
    for i in d: d[i] += 1
    flashing = {i for i in d if d[i] > 9}
    # Process flashing
    while flashing:
        f = flashing.pop()
        d[f] = 0
        count += 1
        for n in neighbours(*f, d): # * unpacks a list, so it makes f into i, j
            d[n] += 1
            if d[n] > 9: flashing.add(n)
    return count

def flash_sim(d: dict, days: int) -> int:
    count = 0
    for n in range(days):
        count+= step_octo(d)
    return count

def find_sync_day(d: dict) -> int:
    for day in range(1,1000):
        if step_octo(d) == 100: return day

def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert flash_sim(test.copy(), 100) == 1656
    print('Part 1: ' + str(flash_sim(data.copy(), 100)))
    # Part 2
    assert find_sync_day(test.copy()) == 195
    print('Part 2: ' + str(find_sync_day(data.copy())))

if __name__ == "__main__":
    main()