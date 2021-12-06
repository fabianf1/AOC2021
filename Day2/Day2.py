# Load data
arr = []
with open("Data.txt", "r") as file:
    for line in file:
        arr.append(line.strip())

print(arr)

# Looper-De-Loop - Part 1 & 2
hor = 0
depth = 0
depth2 = 0
aim = 0
for line in arr:
    command = line.split()
    if command[0] == 'forward':
        hor += int(command[1])
        depth2 += aim*int(command[1])
    elif command[0] == 'up':
        depth -= int(command[1])
        aim -= int(command[1])
    elif command[0] == 'down':
        depth += int(command[1])
        aim += int(command[1])

# Part 1
print(hor)
print(depth)
print(hor * depth)
# Part 2 answer
print(aim)
print(depth2)
print(hor*depth2)
