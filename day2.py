file1 = open('input2.txt', 'r')
Lines = file1.readlines()

correctNumPasswords = 0
wrongNumPasswords = 0

for line in Lines:
    split = line.strip().split(':')
    fullRule = split[0]
    splitRule = fullRule.split(' ')
    letter = splitRule[1]
    splitNumCharacter = splitRule[0].split('-')
    minNumCharacter = int(splitNumCharacter[0])
    maxNumCharacter = int(splitNumCharacter[1])
    password = split[1]

    count = password.count(letter)

    if (count >= minNumCharacter and count <= maxNumCharacter):
        correctNumPasswords += 1
    else:
        wrongNumPasswords += 1

print("Day2 Part 1", correctNumPasswords, wrongNumPasswords)

correctNumPasswords = 0
wrongNumPasswords = 0

for line in Lines:
    split = line.strip().split(':')
    fullRule = split[0]
    splitRule = fullRule.split(' ')
    letter = splitRule[1]
    splitNumCharacter = splitRule[0].split('-')
    minNumCharacter = int(splitNumCharacter[0])
    maxNumCharacter = int(splitNumCharacter[1])
    password = split[1].strip()

    firstLetter = password[minNumCharacter-1]
    secondLetter = password[maxNumCharacter-1]

    if ((firstLetter == letter and secondLetter != letter) or (firstLetter != letter and secondLetter == letter)):
        correctNumPasswords += 1
    else:
        wrongNumPasswords += 1

print("Day2 part 2", correctNumPasswords, wrongNumPasswords)
