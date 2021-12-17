def load_data(path: str):
    return {(x, y): int(e) for x, l in enumerate(open(path))
            for y, e in enumerate(l.strip())}

def neighbours(i: int, j: int, ll: int, v: dict) -> filter:
    return filter(lambda x: 0 <= x[0] < ll and 0 <= x[1] < ll and not v.get(x), [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])

def next_pos(positions: dict, risk: dict) -> int:
    min_risk = 99999
    for i,j in positions:
        if risk[(i,j)] <  min_risk:
            min_risk = risk[(i,j)]
            pos = (i,j)
    positions.pop(pos)
    return pos

def extend_map(d: dict):
    keys = list(d.keys())
    l = keys[-1][0] + 1
    for i, j in d.copy():
        for x in range(0,5):
            for y in range(0,5):
                if x==0 and y == 0:
                    continue
                key = (i+l*x, j+l*y)
                val = ((d[(i,j)] + x + y - 1) % 9)+1
                d[key] = val
    return d

def lowest_risk(d: dict, extend: bool) -> int:
    if extend:
        d = extend_map(d)
    goal = list(d.keys())
    goal = goal[-1]
    ll = goal[0] + 1
    # Dijkstra
    risk_val = d.copy()
    for key in risk_val:
        risk_val[key] = 99999
    risk_val[(0,0)] = 0
    visited = {}
    visitable = { (0,0): 1 }
    pos = (0,0)
    while len(visitable) > 0:
        visited[pos] = 1
        for i, j in neighbours(*pos, ll, visited):
            val = risk_val[pos] + d[(i,j)]
            if val < risk_val[(i,j)]:
                risk_val[(i,j)] = val
            visitable[(i,j)] = 1
        pos = next_pos(visitable, risk_val)

    return risk_val[goal]

def main() -> None:
    # Load data
    test  = load_data('test.txt')
    test2 = load_data('test2.txt')
    data  = load_data('data.txt')
    # Part 1
    assert lowest_risk(test, False) == 40
    print('Part 1: ' + str(lowest_risk(data, False)))
    # Part 2
    assert lowest_risk(test2, False) == 315
    assert lowest_risk(test, True) == 315
    print('Part 2: ' + str(lowest_risk(data, True)))

if __name__ == "__main__":
    main()