groups = open("./input/input_6.txt", 'r').read().split("\n\n")
import string

groupTotal = 0
members = []
for group in groups:
    members         = group.split("\n")
    shortest        = sorted(members, key=len)[0]
    uniqueShortest  = set(shortest)
    candidates = len(uniqueShortest)
    if len(members) > 1:
        for char in uniqueShortest:
            for member in members:
                if char not in member:
                    candidates -= 1
                    break
    
    groupTotal += candidates

print(groupTotal)
