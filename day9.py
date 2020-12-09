file1 = open('input9.txt', 'r')
Lines = file1.readlines()


def populateFromFile():
    data = []
    for line in Lines:
        data.append(line.strip())
    return data


def isPreviousNumbersHasSum(number, previousNumberToCheck, data):
    found = 'no'
    indexRange = range(number-1-previousNumberToCheck, number-1)
    for i in indexRange:
        for j in indexRange:
            if (found == 'yes'):
                break
            if (i != j):
                sum = int(data[i]) + int(data[j])
                if(sum == int(data[number-1])):
                    found = "yes"
                    return -1
    return data[number-1]


def findContiguousSum(answer, data):
    indexRange = range(0, len(data)-1)
    for i in indexRange:
        sum = 0
        iterator = i
        array = []
        while(iterator < len(data)):
            sum += int(data[iterator])
            array.append(int(data[iterator]))
            if (sum == int(answer)):
                return min(array) + max(array)
            else:
                if (sum > int(answer)):
                    break
            iterator += 1


def max(arr):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


def min(arr):
    min = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


data = populateFromFile()
number = 26
previousNumberToCheck = 25
while(len(data) >= number):
    answer = isPreviousNumbersHasSum(number, previousNumberToCheck, data)
    if (answer != -1):
        answer2 = findContiguousSum(answer, data)
        break
    number += 1

print("Part 1 - first number which is not the sum of two of the 25 numbers before it:", answer)
print("Part 2 - the encryption weakness number:", answer2)
