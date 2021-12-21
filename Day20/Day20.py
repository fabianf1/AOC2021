from typing import Tuple

def to_bit(e: str) -> str:
    if e == '.':
        return str(0)
    return str(1)

def load(path: str) -> Tuple[str, dict]:
    data = open(path).read().strip().split('\n\n')

    enhance = ''
    for c in data[0]:
        enhance += to_bit(c)

    image =  {(x, y): to_bit(e) for x, l in enumerate(data[1].splitlines())
            for y, e in enumerate(l.strip())}

    return enhance, image

def enhance_image(e: str, d: dict, num: int) -> dict:
    d = d.copy()
    r = [0,int(pow(len(d),0.5))]
    inf_val = '0'

    for n in range(num):
        r[0] -= 2
        r[1] += 2

        old = d.copy()
        for i in range(r[0], r[1]):
            for j in range(r[0], r[1]):
                # Select data and find new value
                v = ''
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        v += old.get((x, y), inf_val)
                v = int(v,2)
                d[(i,j)] = e[v]
        inf_val = d[(r[0],r[0])]
    return d

def count_bright(d: dict):
    c = 0
    for k,v in d.items():
        if v == '1':
            c += 1
    return c

def do_tests() -> None:
    data = load('Test.txt')
    result = enhance_image(*data, 2)
    assert count_bright(result) == 35
    result = enhance_image(*data, 50)
    assert count_bright(result) == 3351

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('Data.txt')
    result = enhance_image(*data, 2)
    print('Part 1: ' + str(count_bright(result)))
    result = enhance_image(*data, 50)
    print('Part 2: ' + str(count_bright(result)))

if __name__ == "__main__":
    main()