from math import sqrt

def load_data(path: str):
    data =  open(path).read().strip().split(', ')
    return [int(i) for i in data[0][15:].split('..')], [int(j) for j in data[1][2:].split('..')]

def find_most_stylish_shot(_, y_g) -> int:
    v = -y_g[0]-1
    return int(v * (v + 1) / 2)

def find_possible_x(g: list) -> list:
    vel_min = int(0.5 * (sqrt(8 * g[0] + 1) - 1))
    l = []
    for vel in range(vel_min, g[1] + 1):
        step = 0
        x = 0
        s_m = []
        while x < g[1] and vel > step:
            x += vel - step
            step += 1
            if g[0] <= x <= g[1]:
                s_m.append(step)
                if step == vel:
                    s_m.append(-1)
        if len(s_m) > 0:
            l.append([vel, s_m])
    return l

def find_possible_y(g: list) -> list:
    l = []
    for vel in range(g[0], -g[0]):
        step = 0
        y = 0
        s_m = []
        while (y + (vel - step)) >= g[0]:
            y += vel - step
            step += 1
            if g[0] <= y <= g[1]:
                s_m.append(step)
        if len(s_m) > 0:
            l.append([vel, s_m])
    return l

def find_possible_shots(x_g, y_g) -> int:
    # Should merge these functions and clean them up
    x_l = find_possible_x(x_g)
    y_l = find_possible_y(y_g)
    # Combine ==  Check overlap
    combs = {}
    for y_vel, steps in y_l:
        for step in steps:
            for x_vel, steps_x in x_l:
                if step in steps_x or (steps_x[-1] == -1 and step > steps_x[-2]):
                    combs[(x_vel, y_vel)] = 1
    return len(combs)

def do_tests() -> None:
    data = load_data('test.txt')
    assert find_most_stylish_shot(*data) == 45
    assert find_possible_shots(*data) == 112
    print('Tests complete')

def main() -> None:
    do_tests()

    data = load_data('data.txt')
    print('Part 1: ' + str(find_most_stylish_shot(*data)))
    print('Part 2: ' + str(find_possible_shots(*data)))


if __name__ == "__main__":
    main()