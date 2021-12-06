def load_data() -> list:
    # Returns the binary digits separated
    output = []
    with open("Data.txt", "r") as file:
        for line in file:
            output.append(list(line.strip())) #

    return output


def get_bit_count(input) -> list:
    # Init counter
    binLen = len(input[0])
    count = [0] * binLen

    # Count
    for binary in input:
        for i in range(0, binLen):
            count[i] += int(binary[i])

    return count


def get_consumption(input) -> int:
    count = get_bit_count(input)

    # Generate gamma and sigma, and calculate the consumption
    gamma = ''
    sigma = ''
    for n in count:
        if n >= len(input)/2:
            gamma += '1'
            sigma += '0'
        else:
            gamma += '0'
            sigma += '1'

    return int(gamma, 2) * int(sigma, 2)


def get_lifesupport(input) -> int:
    # Get oxygen status
    oxList = input.copy()
    for i in range(0, len(input[0])):
        count = get_bit_count(oxList)
        # Determine
        if count[i] == (len(oxList) / 2):
            bit = 1
        else:
            bit = int(count[i] > len(oxList) / 2)
        # Loop
        for j in range(len(oxList)-1, -1, -1): # Reverse to make sure the index is not messed up
            if not(int(oxList[j][i]) == bit):
                oxList.pop(j)

    # Get CO2 status; Should have made this a function (and read the challenge better)
    CO2List = input.copy()
    for i in range(0, len(input[0])):
        count = get_bit_count(CO2List)
        # Determine
        if count[i] == (len(CO2List)/2):
            bit = 0
        else:
            bit = int(count[i] < len(CO2List) / 2)
        # Loop
        for j in range(len(CO2List)-1, -1, -1):  # Reverse to make sure the index is not messed up
            if len(CO2List) == 1:
                break
            elif not (int(CO2List[j][i]) == bit):
                CO2List.pop(j)

    # Return life support status
    # Splitting the binary right away was maybe not that smart
    return int("".join(oxList[0]), 2) * int("".join(CO2List[0]), 2)


def main() -> None:
    # Load data
    input = load_data()
    # Part 1 - Power consumption
    print("Power consumption: " + str(get_consumption(input)))
    # Part 2 - Oxygen and CO2
    print("Life support rating: " + str(get_lifesupport(input)))


if __name__ == "__main__":
    main()