def load_data(path: str):
    data = open(path).read().strip().split('\n\n')

    paper = {}
    for d in data[0].splitlines():
        x, y = d.split(',')
        paper[(int(x), int(y))] = 1

    operations = []
    for d in data[1].splitlines():
        ax, num = d[11:].split('=')
        operations.append([ax, int(num)])

    return paper, operations

def fold(d: dict, op: list) -> dict:
    keys = list(d.keys()) # List necessary to decouple this variable from the dictionary
    for x, y in keys:
        if op[0] == 'x' and x > op[1]:
            d.pop((x,y))
            x = 2 * op[1] - x
            d[(x, y)] = 1
        elif op[0] == 'y' and y > op[1]:
            d.pop((x,y))
            y = 2 * op[1] - y
            d[(x, y)] = 1
    return d

def dot_after_fold(d: dict, op: list) -> int:
    return len(fold(d, op[0]))

def get_code(d: dict, op: list):
    nx, ny = 0, 0
    for o in op:
        d = fold(d, o)
        if o[0] == 'x':
            nx = o[1]
        else:
            ny = o[1]

    m = []
    for i in range(ny):
        m.append(['.'] * nx)
    for x, y in d:
        m[y][x] = '#'
    for l in m:
        print(l)

def main() -> None:
    # Load data
    t_paper, t_op = load_data('test.txt')
    d_paper, d_op = load_data('data.txt')
    # Part 1
    assert dot_after_fold(t_paper.copy(), t_op) == 17
    print('Part 1: ' + str(dot_after_fold(d_paper.copy(), d_op)))
    # Part 2
    get_code(d_paper, d_op)

if __name__ == "__main__":
    main()