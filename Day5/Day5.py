from collections import defaultdict
from typing import Tuple

def load_data() -> list:
    return [[coords.split(',') for coords in line.split(" -> ")] for line in open('data.txt').read().strip().splitlines()]


def sign(input: int) -> int:
    if input >= 0:
        return 1
    return -1

def process_vent_lines(data: list) -> Tuple[int, int]:
    points = defaultdict(int) # Works much nicer than the python dict
    points_nd = defaultdict(int)
    for line in data:
        # Extract data
        x1 = int(line[0][0])
        y1 = int(line[0][1])
        x2 = int(line[1][0])
        y2 = int(line[1][1])
        #
        dx = max(x1, x2) - min(x1, x2)
        dy = max(y1, y2) - min(y1, y2)
        ix = int(x1 != x2) * sign(x2-x1)
        iy = int(y1 != y2) * sign(y2-y1)
        # Fill
        for i in range(max(dx,dy)+1):
            xc = x1 + ix*i
            yc = y1 + iy*i
            # Increment
            points[xc, yc] += 1
            if x1 == x2 or y1 == y2:
                points_nd[xc, yc] += 1

    # Check number of items > 1
    return len([c for c in points_nd if points_nd[c] > 1]), len([c for c in points if points[c] > 1])

def main() -> None:
    # Load data
    data = load_data()
    # Process
    print(process_vent_lines(data))


if __name__ == "__main__":
    main()