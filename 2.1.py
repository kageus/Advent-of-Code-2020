dataInput = open("./input/input_2.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

itemList = []
for line in lineList:
    itemList.append(line.split(" "))

countValid = 0
for range, needle, haystack in itemList:
    needle = needle.strip(":")
    count = haystack.count(needle)
    bounds = range.split("-")
    if int(bounds[0]) <= count <= int(bounds[1]):
        countValid += 1

print("Valid Passwords:  {}".format(countValid))