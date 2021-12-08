def load_data(path: str) -> list:
    output = []
    for x, y in [x.split('|') for x in open(path).read().strip().splitlines()]:
        # This creates a dictionary; Key corresponds to the length;
        # Because only 1,4,7,8 have a unique length they are the only ones certain to be in here
        output.append([{len(s): set(s) for s in x.split()}, y.split()])
    return output


def count_unique_numbers_in_output(data: list) -> int:
    count = 0
    for line in data:
        count += len([len(x) for x in line[1] if len(x) not in [5,6]])
    return count


def sum_output_numbers(data: list) -> int:
    c = 0
    for l in data:
        n = ''
        for o in map(set, l[1]): # Map transforms every entry in l[1] into a set
            match len(o), len(o&l[0][4]), len(o&l[0][2]): # Differentiate between numbers using length, overlap with 4 and overlap with 1
                case 2, _, _: n += '1'
                case 3, _, _: n += '7'
                case 4, _, _: n += '4'
                case 7, _, _: n += '8'
                case 5, 2, _: n += '2'
                case 5, 3, 1: n += '5'
                case 5, 3, 2: n += '3'
                case 6, 4, _: n += '9'
                case 6, 3, 1: n += '6'
                case 6, 3, 2: n += '0'
        c += int(n)
    return c


def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert count_unique_numbers_in_output(test) == 26
    print(count_unique_numbers_in_output(data))
    # Part 2
    assert sum_output_numbers(test) == 61229
    print(sum_output_numbers(data))


if __name__ == "__main__":
    main()