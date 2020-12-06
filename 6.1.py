data = open("./input/input_6.txt", 'r').read().split("\n\n")
import string

counts = 0
count  = 0

for line in data:
    line = line.replace("\n", "")
    for char in string.ascii_lowercase:
        if char in line:  count += 1
    counts += count
    count = 0

print(counts)