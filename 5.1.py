data = open("./input/input_5.txt", 'r').read().split("\n")

def parseIndex(parsable, range):
    index = 0
    for step in parsable:
        if step in ["L", "F"]:
            range = range / 2
            continue
        else:
            index += int(range / 2)
            range  = int(range / 2)
    return index

highest = 0
for line in data:
    row     = line[:7]
    column    = line[7:]
    row     = parseIndex(row, 128)
    column    = parseIndex(column, 8)
    seatId  = (row * 8) + column
    if seatId > highest: highest = seatId

print(highest)

