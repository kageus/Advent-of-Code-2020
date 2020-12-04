# find any given value of a repeating string at X coordinate
def lineValueAtTarget(line, target):
    if target > len(line):
        target = target % len(line)
    return line[target]

dataInput = open("./input/input_3.txt").read().split("\n")

treeCount       = 0
currentLocation = 0

for line in dataInput:
    valueAtLocation = lineValueAtTarget(line, currentLocation)
    
    if valueAtLocation == "#":
        treeCount += 1

    currentLocation += 3

print(treeCount)
