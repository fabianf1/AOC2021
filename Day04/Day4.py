from typing import Tuple


def load_data() -> Tuple[list, list]:
    # Load data
    data = [x for x in open('data.txt').read().strip().split('\n\n')]
    # Extract draw numbers
    numbers = data[0].split(',')
    # Extract and split boards
    boards = data[1:len(data)]
    boards = [line.split() for line in boards]
    # Return
    return numbers, boards


def do_bingo(numbers: list, boards: list) -> Tuple[int, int]:
    win_draw = len(numbers)
    last_win_draw = 0

    for board in boards:
        # Init variables
        hit_list = []
        not_hit_list = list(range(0, 25))
        num_draws = 0
        won = False
        # Loop over numbers
        for number in numbers:
            num_draws += 1
            # Find the index of the number and add it to the hit_list, or returns -1 if not found
            # No clue how it works though...
            # Can be done with index(number) as well, but then I have to deal with an error if not found
            index = next((i for i, x in enumerate(board) if x == number), -1)
            if index > -1:
                hit_list.append(index)
                not_hit_list.remove(index)

            # Check for horizontal rows
            for i in range(0, 5):
                if all(x in hit_list for x in list(range(i*5, (i+1)*5))):
                    won = True
            # Check Vertical rows
            for i in range(0, 5):
                if all(x in hit_list for x in list(range(i, 25, 5))):
                    won = True

            # Calculate points if finished
            if won:
                # First win board
                if num_draws < win_draw:
                    win_draw = num_draws
                    points = 0
                    for idx in not_hit_list:
                        points += int(board[idx])
                    points *= int(number)
                # Last win board
                if num_draws > last_win_draw:
                    last_win_draw = num_draws
                    points_last = 0
                    for idx in not_hit_list:
                        points_last += int(board[idx])
                    points_last *= int(number)

                # Make sure to break :)
                break

    # Return
    return points, points_last


def main() -> None:
    # Load data
    numbers, boards = load_data()
    # Simulate Bingo
    print('First and last win scores: ' + str(do_bingo(numbers, boards)))


if __name__ == "__main__":
    main()
