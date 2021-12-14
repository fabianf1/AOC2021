from typing import Callable

def load_data(path: str) -> list:
   return [int(line) for line in open(path).read().strip().split(',')]


def find_fuel_usage(data: list, fuel: Callable[[int], int]) -> int:
    return min([sum([fuel(abs(crab - i)) for crab in data]) for i in range(min(data),max(data)+1)])


def main() -> None:
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Part 1
    dist = lambda d: d
    assert find_fuel_usage(test, dist) == 37
    print("Fuel usage with constant fuel usage: " + f"{find_fuel_usage(data, dist):.0f}")
    # Part 2
    dist = lambda d: d*(d+1)/2
    assert find_fuel_usage(test, dist) == 168
    print("Fuel usage with linear fuel usage: " + f"{find_fuel_usage(data, dist):.0f}")


if __name__ == "__main__":
    main()