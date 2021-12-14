from collections import defaultdict

def load_data(path: str) -> list:
   return [int(line) for line in open(path).read().strip().split(',')]


def sim_lanternfish(data: list, days: int) -> int:
    # Copy data into new structure
    num_fish = defaultdict(int)
    for fish in data:
        num_fish[fish] += 1

    # Loop time
    for i in range(days):
        # Decrement timers
        for j in range(0, 9):
            num_fish[j-1] = num_fish[j]
        # Process new-spawn
        num_fish[6] += num_fish[-1]
        num_fish[8] = num_fish[-1]

    # Return number of fish
    num_fish[-1] = 0
    return sum([value for key, value in num_fish.items()])


def main() -> None:
    # Load data
    test = load_data('test.txt')
    data = load_data('data.txt')
    # Test data
    assert sim_lanternfish(test.copy(), 18) == 26
    assert sim_lanternfish(test.copy(), 80) == 5934
    assert sim_lanternfish(test.copy(), 256) == 26984457539
    # Part 1
    print("Number of lanternfish at day 80: " + str(sim_lanternfish(data.copy(), 80)))
    # Part 2
    print("Number of lanternfish at day 256: " + str(sim_lanternfish(data.copy(), 256)))


if __name__ == "__main__":
    main()