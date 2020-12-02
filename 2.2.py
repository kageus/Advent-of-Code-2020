dataInput = open("./input/input_2.txt").read().split("\n")

lineList = []
for line in dataInput:
    lineList.append(str(line))

itemList = []
for line in lineList:
    itemList.append(line.split(" "))

countValid = 0
for rule, needle, haystack in itemList:
    needle = needle.strip(":")
    targetx, targety = [int(x) for x in rule.split("-")]
    # checking haystack index of targets - 1 b/c provided targets are not 0 indexed
    if haystack[targetx - 1] == needle and haystack[targety - 1] == needle:
        continue
    if haystack[targetx - 1] == needle or haystack[targety - 1] == needle:
        countValid += 1

print("Valid Passwords:  {}".format(countValid))