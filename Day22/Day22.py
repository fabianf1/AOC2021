def load(path: str) -> list:
    data = open(path).read().strip().splitlines()

    output = []
    for line in data:
        action, coord = line.split(' ')
        action = action=='on'
        coord = [[int(x) for x in c[2:].split('..')] for c in coord.split(',')]
        output.append([action, coord])

    return output

def volume(d: list) -> int:
    return (d[0][1]+1-d[0][0])*(d[1][1]+1-d[1][0])*(d[2][1]+1-d[2][0])

def overlap(d1, d0):
    x = [max([d1[0][0], d0[0][0]]), min([d1[0][1], d0[0][1]])]
    y = [max([d1[1][0], d0[1][0]]), min([d1[1][1], d0[1][1]])]
    z = [max([d1[2][0], d0[2][0]]), min([d1[2][1], d0[2][1]])]
    if x[1] < x[0] or y[1] < y[0] or z[1] < z[0]:
        return -1
    return x, y, z


def cubes_after_boot(d: list, full_range: bool):
    v = [[True, d[0][1]]]
    c = volume(d[0][1])

    for i in range(1, len(d)):
        a, p = d[i]
        if not full_range:
            if p[0][0] < -50 or p[1][0] < -50 or p[1][0] < -50 or p[0][1] > 50 or p[1][1] > 50 or p[1][1] > 50:
                continue

        j_max = len(v)
        if d[i][0]:
            v.append([True, p])
            c += volume(p)

        # Can probably improve this by removing unnecesary actions
        for j in range(j_max):
            if v[j][0]:
                o = overlap(v[j][1], p)
                if o != -1:
                    v.append([False, o])
                    c -= volume(o)
            else:
                o = overlap(v[j][1], p)
                if o != -1:
                    v.append([True, o])
                    c += volume(o)

    return c

def do_tests() -> None:
    data = load('Small.txt')
    assert cubes_after_boot(data[:1], False) == 27
    assert cubes_after_boot(data[:2], False) == 46
    assert cubes_after_boot(data[:3], False) == 38
    assert cubes_after_boot(data[:4], False) == 39

    data = load('Test.txt')
    assert cubes_after_boot(data, False) == 590784

    data = load('Test2.txt')
    assert cubes_after_boot(data, True) == 2758514936282235

    print('Tests complete')

def main() -> None:
    do_tests()

    data = load('Data.txt')
    print('Part 1: ' + str(cubes_after_boot(data, False)))
    print('Part 2: ' + str(cubes_after_boot(data, True)))

if __name__ == "__main__":
    main()