# find any given value of a repeating string at X coordinate
def lineValueAtTarget(line, target):
    if target >= len(line):
        target = target % len(line)
    return line[target]

def countTreesForSlope(right, down):
    dataInput = open("./input/input_3.txt").read().split("\n")

    treeCount       = 0
    currentLocation = 0

    for vertical, line in enumerate(dataInput):
        if vertical % down == 0:
            valueAtLocation = lineValueAtTarget(line, currentLocation)
            
            if valueAtLocation == "#":
                treeCount += 1

            currentLocation += right

    return treeCount

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
treesHit = []

for slope in slopes:
    treesHit.append(countTreesForSlope(slope[0], slope[1]))

finalAnswer = 1
for x in treesHit:
    finalAnswer *= x
    print(finalAnswer)

