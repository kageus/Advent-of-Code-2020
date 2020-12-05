dataInput = open("./input/input_4.txt").read().split("\n")

def splitInput(dataInput):
    passports = []
    passport  = ""
    for line in dataInput:
        if(line == ""):
            passports.append(passport)
            passport = ""
        else:
            passport += line
    # ugly way to handle last passport
    passports.append(passport)
    return passports


passports = splitInput(dataInput)

valid = 0
for x, passport in enumerate(passports):
    matches = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    if all(x in passport for x in matches):
        valid += 1


print(valid)