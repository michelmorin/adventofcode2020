file1 = open('input10test2.txt', 'r')
Lines = file1.readlines()

variance = 1


def populateFromFile():
    data = [0]
    for line in Lines:
        data.append(int(line.strip()))
    return data

#[0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
#
# everytime there is change from origina, need to save that array, and have that run the whole thing again.


def recursive(data, index, previousUsed):
    global variance

    index2 = 1

    print("new recursive", data, index-1, data[index-index2])

    for entry in data:
        if (index - index2 >= 0):
            if (data[index-index2] != previousUsed and data[index] - data[index-index2] <= 3):
                print("add new combination",
                      data[index], data[index-index2], previousUsed)
                variance += 1
                #newData = data.remove(index+1)
                #newData = data.copy()
                #recursive(newData, len(newData)-1, data[len(newData)-2])
            else:
                if(data[index] - data[index-index2] > 3):
                    print("Not a new combination",
                          data[index], data[index-index2], previousUsed)
                    recursive(data, index-1, data[index-index2])
                    break
                else:
                    print("Not a new combination, but maybe next one",
                          data[index], data[index-index2], previousUsed)
        index2 += 1
    return variance


data = sorted(populateFromFile())
data.append(data[-1] + 3)

diff1count = 0
diff3count = 0
previous = 0

#[0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]

for adapter in data:
    diff = adapter - previous
    if (diff == 1):
        diff1count += 1
    else:
        if (diff == 3):
            diff3count += 1
    previous = adapter

print("Part 1 - answer:", diff1count*diff3count)

print(data)
recursive(data, len(data)-1, data[len(data)-2])

print("Part 2 - answer:", variance)
