file1 = open('input10.txt', 'r')
Lines = file1.readlines()


def populateFromFile():
    data = [0]
    for line in Lines:
        data.append(int(line.strip()))
    return data


data = sorted(populateFromFile())
data.append(data[-1] + 3)

diff1count = 0
diff3count = 0
previous = 0

for adapter in data:
    diff = adapter - previous
    if (diff == 1):
        diff1count += 1
    else:
        if (diff == 3):
            diff3count += 1
    previous = adapter

print("Part 1 - answer:", diff1count*diff3count)

numbers = [0] + data
answers = [0 for n in data]


def ways(somenumbers, offset):
    if len(somenumbers) < 3:
        return 1
    numways = 0
    idxd = 1
    while idxd < len(somenumbers) and somenumbers[idxd] < somenumbers[0] + 4:
        if answers[offset + idxd] == 0:
            newanswer = ways(somenumbers[idxd:], offset + idxd)
            numways += newanswer
            answers[offset + idxd] = newanswer
        else:
            numways += answers[offset + idxd]
        idxd += 1
    return numways


print("Part 2 - answer:", ways(numbers, 0)/2)
