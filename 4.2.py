import re
dataInput = open("./input/input_4.txt").read().split("\n")

def splitInput(dataInput):
    passports = []
    passport  = ""
    for line in dataInput:
        if(line != ""):
            if passport == "":
                passport += line
            else:
                passport += " " + line
        else:
            passports.append(passport)
            passport = ""
    # ugly way to handle appending last passport
    passports.append(passport)
    return passports

def xyrCheck(passport):
    yearChecks = [['byr', 1920, 2002],['iyr', 2010, 2020],['eyr', 2020, 2030]]
    for check in yearChecks:
        docYear = passport[passport.find(check[0]):]
        if(docYear.find(" ") >= 0):
            docYear =  docYear[:docYear.find(" ")]
        docYear = int(docYear[4:])
        if docYear < check[1] or docYear > check[2]:
            return 0
    return 1

def hgtCheck(passport):
    height = passport[passport.find('hgt'):]
    # if not the last element slice off extra
    if(height.find(" ") >= 0):
        height =  height[:height.find(" ")]
    scale = height[-2:]
    if scale not in ['cm','in']:
        return 0
    height = int(height[4:-2])
    heightChecks = [['cm', 150, 193],['in', 59, 76]]
    for check in heightChecks:
        if scale == check[0]:
            if height < check[1] or height > check[2]:
                return 0
    return 1

def hclCheck(passport):
    hair = passport[passport.find('hcl'):]
    # if not the last element slice off extra
    if(hair.find(" ") >= 0):
        hair =  hair[:hair.find(" ")]
    hair = hair[4:]
    valid = re.search("^#([a-fA-F0-9]{6})$", hair)
    if valid == None:
        return 0
    return 1

def eclCheck(passport):
    eye = passport[passport.find('ecl'):]
    # if not the last element slice off extra
    if(eye.find(" ") >= 0):
        eye =  eye[:eye.find(" ")]
    eye = eye[4:]
    if eye not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return 0
    return 1

def pidCheck(passport):
    passportNumber = passport[passport.find('pid'):]
    # if not the last element slice off extra
    if(passportNumber.find(" ") >= 0):
        passportNumber =  passportNumber[:passportNumber.find(" ")]
    passportNumber = passportNumber[4:]
    valid = re.search("^\\d{9}$", passportNumber)
    if valid == None:
        return 0
    return 1

def validateFields(passport):
    if(not xyrCheck(passport)): return 0
    if(not hgtCheck(passport)): return 0
    if(not hclCheck(passport)): return 0
    if(not eclCheck(passport)): return 0
    if(not pidCheck(passport)): return 0
    return 1



validPassports = []
passports = splitInput(dataInput)
totalValid = 0
for x, passport in enumerate(passports):
    matches = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    # all fields present
    if all(x in passport for x in matches):
        # all fields valid
        totalValid += validateFields(passport)
print(totalValid)