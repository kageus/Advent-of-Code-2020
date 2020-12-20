lines = open("./input/test_input_7.txt", 'r').read().split("\n")

bags = {}
# Build a dictionary
for line in lines:
    bag = {}
    key, values = line.split(" contain ")
    key = key.split(" bags")[0]
    values = values.split(", ")
    for value in values:
        value = value.split(" bag")[0]
        quantity, descriptor = value.split(" ", 1)
        if(quantity != "no"):
            bag[descriptor] = int(quantity)
            bags[key] = bag
        else:
            bags[key] = {}

unpackedBags = {}
# Unpack the dictionary
for key, values in bags.items():
    unpackedBags[key] = values
    for value in values:
        for innerbag in bags[value]:
            unpackedBags[key][innerbag] = bags[innerbag]
        print(unpackedBags)
