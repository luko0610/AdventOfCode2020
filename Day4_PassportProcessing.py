import re
fourNumbersOnly = re.compile('\d{4}')
heightInch = re.compile('\d+in')
heightCm = re.compile('\d+cm')
hairColor = re.compile('#+[0-9A-Fa-f]{6}')
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
nineDigits = re.compile('\d{9}')

# Parses the passports in the file with the given path
# and returns them as an array of key/value pairs.
def parsePassports(fileName):
    passports = []
    current = {}
    with open(fileName) as f:
        for line in f:
            if line != "\n":
                line = line.rstrip().split(" ")
                
                # split all key value pairs and set them in the passport object.
                line = [field.split(":") for field in line]
                for field in line:
                    current[field[0]] = field[1]
            # current passport finished -> append and set pasport to empty object.
            else:
                passports.append(current)
                current = {}
                
    # last passport has no \n afterwards, so still needs to be appended.
    passports.append(current)
    return passports

# validates the given passport according to the policy describen in part two.
def validatePassport(pp):

    # Checking birthyear.
    if(fourNumbersOnly.match(pp["byr"]) != None):
        by = int(pp["byr"])
        if(by < 1920 or by > 2002):
            return False
    else:
        return False

    # Checking issuer year.
    if(fourNumbersOnly.match(pp["iyr"]) != None):
        by = int(pp["iyr"])
        if(by < 2010 or by > 2020):
            return False
    else:
        return False

    # Checking expiration year.
    if(fourNumbersOnly.match(pp["eyr"]) != None):
        by = int(pp["eyr"])
        if(by < 2020 or by > 2030):
            return False
    else:
        return False

    # Checking height.
    if((heightInch.match(pp["hgt"]) != None
        or heightCm.match(pp["hgt"]) != None)):

        by = int(pp["hgt"].replace("in", "") if heightInch.match(pp["hgt"]) else pp["hgt"].replace("cm", ""))

        if(heightInch.match(pp["hgt"]) != None and (by < 59 or by > 76)):
            return False
        elif(heightCm.match(pp["hgt"]) != None and (by < 150 or by > 193)):
            return False
    else:
        return False

    # Checking hair color.
    if(not hairColor.match(pp["hcl"])):
        print('hairColor failed ' + pp["hcl"])
        return False

    # Checking eye color.
    if(pp["ecl"] not in eyeColors):
        print('eyecolor failed ' + pp["ecl"])
        return False

    # Checking passport id.
    if(nineDigits.match(pp["pid"]) == None):
        print('pid failed ' + pp["pid"])
        return False

    return True


passports = parsePassports('./input_Day4.txt')
print('parsed' + str(len(passports)))
validCount = 0

for pp in passports:
    if("byr" in pp.keys() and
       "iyr" in pp.keys() and
       "eyr" in pp.keys() and
       "hgt" in pp.keys() and
       "hcl" in pp.keys() and
       "ecl" in pp.keys() and
       "pid" in pp.keys()):

        if(validatePassport(pp)):
            validCount += 1

print(str(validCount) + " passports valid")
