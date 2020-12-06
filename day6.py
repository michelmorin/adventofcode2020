file1 = open('input6.txt', 'r')
Lines = file1.readlines()

sum = 0
sum2 = 0
groupAnswers = {}
numPeopleInGroup = 0

for line in Lines:
    line = line.strip()
    if (line == ""):
        # new group reset and count
        sum += len(groupAnswers)
        for value in groupAnswers.values():
            if (value == numPeopleInGroup):
                sum2 += 1
        groupAnswers.clear()
        numPeopleInGroup = 0
    else:
        numPeopleInGroup += 1
        for a in line:
            if groupAnswers.get(a):
                groupAnswers[a] += 1
            else:
                groupAnswers[a] = 1

# Last One
sum += len(groupAnswers)
for value in groupAnswers.values():
    # print(value)
    if (value == numPeopleInGroup):
        sum2 += 1
print("Part 1 - Sum of the counts:", sum)
print("Part 2 - Sum of the counts:", sum2)
