file1 = open('input.txt', 'r')
Lines = file1.readlines()

inputValues = []

for line in Lines:
    inputValues.insert(1, int(line.strip()))

found = 'no'
count = 0
for count, item in enumerate(inputValues):
    count2 = 0
    if (found == 'yes'):
        break
    for count2, item2 in enumerate(inputValues):
        if (found == 'yes'):
            break
        if (count != count2):
            sum = inputValues[count] + inputValues[count2]
            if(sum == 2020):
                found = "yes"
                multiplied = inputValues[count] * inputValues[count2]
                print("Part 1 sum answer is:", multiplied)

found = 'no'
count = 0
for count, item in enumerate(inputValues):
    count2 = 0
    if (found == 'yes'):
        break
    for count2, item2 in enumerate(inputValues):
        count3 = 0
        if (found == 'yes'):
            break
        for count3, item3 in enumerate(inputValues):
            if (found == 'yes'):
                break
            if (count != count2):
                sum = inputValues[count] + \
                    inputValues[count2] + inputValues[count3]
                if(sum == 2020):
                    found = "yes"
                    multiplied = inputValues[count] * \
                        inputValues[count2] * inputValues[count3]
                    print("Part 2 sum answer is:", multiplied)
