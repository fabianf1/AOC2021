from statistics import mean, median

def load_data(path: str) -> list:
   return [int(line) for line in open(path).read().strip().split(',')]


def find_fuel_usage(data: list, linear_fuel: bool) -> int:
    if linear_fuel:
        best_guess = round(mean(data)) # This is close to the best position
        fuel = lambda d: d*(d+1)/2
        return min([sum([fuel(abs(crab-best_guess  )) for crab in data]),
                    sum([fuel(abs(crab-best_guess-1)) for crab in data]),
                    sum([fuel(abs(crab-best_guess+1)) for crab in data])])
    else:
        best_pos = median(data) # This is guaranteed to be the best position
        return sum([abs(crab-best_pos) for crab in data])


def main() -> None:
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    assert find_fuel_usage(test, False) == 37
    print("Fuel usage with constant fuel usage: " + f"{find_fuel_usage(data, False):.0f}")
    # Part 2
    assert find_fuel_usage(test, True) == 168
    print("Fuel usage with linear fuel usage: " + f"{find_fuel_usage(data, True):.0f}")


if __name__ == "__main__":
    main()