
def load(path: str) -> list:
    data = open(path).read().strip().split('\n')
    return [int(data[0][-1]), int(data[1][-1])]

def deterministic_score(data: list) -> int:
    d = 1
    d_c = 0
    scores = [0, 0]
    pos = data.copy()
    i = 0
    #
    while max(scores)<1000:
        s = d + ((d % 100) + 1) + ((d+1) % 100) + 1
        d = ((d+2) % 100) + 1
        d_c += 3
        pos[i] = (pos[i]+s-1) % 10 + 1
        scores[i] += pos[i]
        i = (i+1) % 2

    return min(scores) * d_c

def quantum_score(d: list) -> int:
    throws = {}
    for i in range(1,4):
        for j in range(1, 4):
            for k in range(1, 4):
                throws[i+j+k] = throws.get(i+j+k, 0) + 1

    q = {}
    for i in throws:
        p = (d[0]+i-1) % 10 + 1
        q[(p, p, d[1], 0, False)] = throws[i]

    c = [0,0]
    while len(q) > 0:
        for key in q:
            for i in throws:
                p1, s1, p2, s2, t = key
                num = q[key] * throws[i]
                if t:
                    p1 = (p1 + i - 1) % 10 + 1
                    s1 = s1 + p1
                else:
                    p2 = (p2 + i - 1) % 10 + 1
                    s2 = s2 + p2
                if s1 >= 21:
                    c[0] += num
                elif s2 >= 21:
                    c[1] += num
                else:
                    keyN = (p1, s1, p2, s2, not t)
                    q[keyN] = q.get(keyN, 0) + num
            # Remove processed
            q.pop(key)
            break
    return max(c)

def do_tests() -> None:
    data = load('Test.txt')
    assert deterministic_score(data) == 739785
    assert quantum_score(data) == 444356092776315

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('Data.txt')
    print('Part 1: ' + str(deterministic_score(data)))
    print('Part 1: ' + str(quantum_score(data)))

if __name__ == "__main__":
    main()