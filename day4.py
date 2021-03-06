file1 = open('input4.txt', 'r')
Lines = file1.readlines()

numValidPassports = 0

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False

for line in Lines:
    splitSpace = line.strip().split(' ')
    for data in splitSpace:
        splitData = data.strip().split(':')
        if (splitData[0] == 'byr'):
            byr = True
        if (splitData[0] == 'iyr'):
            iyr = True
        if (splitData[0] == 'eyr'):
            eyr = True
        if (splitData[0] == 'hgt'):
            hgt = True
        if (splitData[0] == 'hcl'):
            hcl = True
        if (splitData[0] == 'ecl'):
            ecl = True
        if (splitData[0] == 'pid'):
            pid = True
        if (splitData[0] == 'cid'):
            cid = True

    if (line.strip() == ""):
        if (byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True):
            numValidPassports += 1

        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False

if (byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True):
    numValidPassports += 1

print("Part 1 - Total Number of Valid Passports:", numValidPassports)

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False

numValidPassports = 0

for line in Lines:
    splitSpace = line.strip().split(' ')
    for data in splitSpace:
        splitData = data.strip().split(':')
        if (splitData[0] == 'byr' and int(splitData[1]) >= 1920 and int(splitData[1]) <= 2002):
            byr = True
        if (splitData[0] == 'iyr' and int(splitData[1]) >= 2010 and int(splitData[1]) <= 2020):
            iyr = True
        if (splitData[0] == 'eyr' and int(splitData[1]) >= 2020 and int(splitData[1]) <= 2030):
            eyr = True
        if (splitData[0] == 'hgt'):
            if (splitData[1].endswith('cm')):
                heightNumber = int(splitData[1].replace('cm', ''))
                if (heightNumber >= 150 and heightNumber <= 193):
                    hgt = True
            if (splitData[1].endswith('in')):
                heightNumber = int(splitData[1].replace('in', ''))
                if (heightNumber >= 59 and heightNumber <= 76):
                    hgt = True
        if (splitData[0] == 'hcl'):
            if (splitData[1][0] == "#" and len(splitData[1]) == 7):
                hclColour = splitData[1].replace('#', '')

                hcl = True
                for char in hclColour:
                    if (char.isalnum()):
                        if(char.isalpha()):
                            if(char != 'a' and char != 'b' and char != 'c' and char != 'd' and char != 'e' and char != 'f'):
                                hcl = False
                                print(char, "charter not in range")
                    else:
                        hcl = False
                        print(char, "is not alnum")

                if (hcl == False):
                    print(splitData[1])

        if (splitData[0] == 'ecl'):
            if (splitData[1] == "amb" or splitData[1] == "blu" or splitData[1] == "brn" or splitData[1] == "gry" or splitData[1] == "grn" or splitData[1] == "hzl" or splitData[1] == "oth"):
                ecl = True
        if (splitData[0] == 'pid' and len(splitData[1]) == 9):
            pid = True
        if (splitData[0] == 'cid'):
            cid = True

    if (line.strip() == ""):
        if (byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True):
            numValidPassports += 1

        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False

if (byr == True and iyr == True and eyr == True and hgt == True and hcl == True and ecl == True and pid == True):
    numValidPassports += 1

print("Part 2 - Total Number of Valid Passports:", numValidPassports)
