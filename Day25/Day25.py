def load(path: str):
    return {(x, y): e for x, l in enumerate(open(path).read().splitlines())
            for y, e in enumerate(l)}

def finishing_step(d):
    k = list(d.keys())[-1]
    i_max = k[0] + 1
    j_max = k[1] + 1

    p = []
    steps = 0
    while p != d:
        steps += 1
        # Pass 1: Right moving
        p = d.copy()
        for (i,j), c in p.items():
            if c == 'v' or c == '.':
                continue
            j2 = (j + 1) % j_max
            if  p[(i, j2)] == '.':
                d[(i, j )] = '.'
                d[(i, j2)] = '>'
        # Pass 2: Down moving
        p2 = d.copy()
        for (i, j), c in p2.items():
            if c == '>' or c == '.':
                continue
            i2 = (i + 1) % i_max
            if  p2[(i2, j)] == '.':
                d[(i , j)] = '.'
                d[(i2, j)] = 'v'

    return steps

def do_tests() -> None:
    # Multiplication test
    data = load('Test.txt')
    assert finishing_step(data) == 58

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('Data.txt')
    print("Part 1: " + str(finishing_step(data)))

if __name__ == "__main__":
    main()