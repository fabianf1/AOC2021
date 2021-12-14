# Numpy :)
import numpy as np
arr = [] #np.array

#  Load file
with open("Data.txt", "r") as file:
    for line in file:
        arr.append(int(line)) # Int to prevent string and remove the newline

print(arr)
print(len(arr))

# Day 1 - Part 1
numInc = 0
for i in range(1,len(arr)):
    if arr[i-1]<arr[i]:
        numInc += 1
print(numInc)

# Day 1 - Part 1 re-do
print( sum( (np.array(arr[1:len(arr)]) - np.array(arr[0:len(arr)-1]) ) > 0) )

# Day 1 - Part 2
arrC = np.convolve(arr, [1, 1, 1],'valid')
print(arrC)
print(len(arrC))
numInc = 0

for i in range(1,len(arrC)):
    if arrC[i-1]<arrC[i]:
        numInc += 1
print(numInc)

