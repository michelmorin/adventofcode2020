file1 = open('input11.txt', 'r')
Lines = file1.readlines()

changeHappened = -1


def numColRows():
    col, row = 0, 0
    for line in Lines:
        line = line.strip()
        col = len(line)
        row += 1
    return col, row


def populateFromFile():
    col, row = numColRows()
    array = [[0 for x in range(col)] for y in range(row)]
    lineCount = 0
    for line in Lines:
        charCount = 0
        line = line.strip()
        for charCount, char in enumerate(line):
            array[lineCount][charCount] = char
        lineCount += 1
    return array


def processWaitingArea(data):
    global changeHappened
    col, row = numColRows()
    changeHappened = 0
    data2 = [[0 for x in range(col)] for y in range(row)]
    for rowCount, row in enumerate(data):
        for colCount, seat in enumerate(row):
            # check what is around
            if (data[rowCount][colCount] == "L"):
                adjacentSeatOccupied = 0
                if (rowCount > 0 and colCount > 0 and data[rowCount-1][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount > 0 and data[rowCount-1][colCount] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount > 0 and colCount < len(row)-1 and data[rowCount-1][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (colCount > 0 and data[rowCount][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (colCount < len(row)-1 and data[rowCount][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (rowCount < len(data)-1 and colCount > 0 and data[rowCount+1][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount < len(data)-1 and data[rowCount+1][colCount] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount < len(data)-1 and colCount < len(row)-1 and data[rowCount+1][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (adjacentSeatOccupied == 0):
                    data2[rowCount][colCount] = "#"
                    changeHappened += 1
                else:
                    data2[rowCount][colCount] = "L"
            if (data[rowCount][colCount] == "#"):
                # If find anyone sitting adjacent then return to L
                adjacentSeatOccupied = 0
                if (rowCount > 0 and colCount > 0 and data[rowCount-1][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount > 0 and data[rowCount-1][colCount] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount > 0 and colCount < len(row)-1 and data[rowCount-1][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (colCount > 0 and data[rowCount][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (colCount < len(row)-1 and data[rowCount][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (rowCount < len(data)-1 and colCount > 0 and data[rowCount+1][colCount-1] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount < len(data)-1 and data[rowCount+1][colCount] == "#"):
                    adjacentSeatOccupied += 1
                if (rowCount < len(data)-1 and colCount < len(row)-1 and data[rowCount+1][colCount+1] == "#"):
                    adjacentSeatOccupied += 1

                if (adjacentSeatOccupied >= 4):
                    data2[rowCount][colCount] = "L"
                    changeHappened += 1
                else:
                    data2[rowCount][colCount] = "#"
            if (data[rowCount][colCount] == "."):
                data2[rowCount][colCount] = "."
    return data2


def processWaitingArea2(data):
    global changeHappened
    col, row = numColRows()
    changeHappened = 0
    data2 = [[0 for x in range(col)] for y in range(row)]
    for rowCount, row in enumerate(data):
        for colCount, seat in enumerate(row):
            # check what is around
            if (data[rowCount][colCount] == "L"):
                adjacentSeatOccupied = 0
                found = True
                index = 0
                while(found):
                    if (rowCount > index and colCount > index):
                        if(data[rowCount-(index+1)][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if (data[rowCount-(index+1)][colCount-(index+1)] == "L"):
                            break
                        if (data[rowCount-(index+1)][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if(rowCount > index):
                        if (data[rowCount-(index+1)][colCount] == "."):
                            index += 1
                            continue
                        if (data[rowCount-(index+1)][colCount] == "L"):
                            break
                        if (data[rowCount-(index+1)][colCount] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount > index and colCount < len(row)-(index+1)):
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "L"):
                            break
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                index = 0
                while(found):
                    if (colCount > index):
                        if(data[rowCount][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount][colCount-(index+1)] == "L"):
                            break
                        if(data[rowCount][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (colCount < len(row)-(index+1)):
                        if (data[rowCount][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if (data[rowCount][colCount+(index+1)] == "L"):
                            break
                        if (data[rowCount][colCount+(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1) and colCount > index):
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1)):
                        if(data[rowCount+(index+1)][colCount] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1) and colCount < len(row)-(index+1)):
                        if(data[rowCount+index+1][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount+index+1] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount+index+1] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                if (adjacentSeatOccupied == 0):
                    data2[rowCount][colCount] = "#"
                    changeHappened += 1
                else:
                    data2[rowCount][colCount] = "L"

            if (data[rowCount][colCount] == "#"):
                adjacentSeatOccupied = 0
                found = True
                index = 0
                while(found):
                    if (rowCount > index and colCount > index):
                        if(data[rowCount-(index+1)][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if (data[rowCount-(index+1)][colCount-(index+1)] == "L"):
                            break
                        if (data[rowCount-(index+1)][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if(rowCount > index):
                        if (data[rowCount-(index+1)][colCount] == "."):
                            index += 1
                            continue
                        if (data[rowCount-(index+1)][colCount] == "L"):
                            break
                        if (data[rowCount-(index+1)][colCount] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount > index and colCount < len(row)-(index+1)):
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "L"):
                            break
                        if(data[rowCount-(index+1)][colCount+(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                index = 0
                while(found):
                    if (colCount > index):
                        if(data[rowCount][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount][colCount-(index+1)] == "L"):
                            break
                        if(data[rowCount][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (colCount < len(row)-(index+1)):
                        if (data[rowCount][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if (data[rowCount][colCount+(index+1)] == "L"):
                            break
                        if (data[rowCount][colCount+(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1) and colCount > index):
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount-(index+1)] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1)):
                        if(data[rowCount+(index+1)][colCount] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break
                index = 0
                while(found):
                    if (rowCount < len(data)-(index+1) and colCount < len(row)-(index+1)):
                        if(data[rowCount+index+1][colCount+(index+1)] == "."):
                            index += 1
                            continue
                        if(data[rowCount+(index+1)][colCount+index+1] == "L"):
                            break
                        if(data[rowCount+(index+1)][colCount+index+1] == "#"):
                            adjacentSeatOccupied += 1
                            break
                    else:
                        break

                if (adjacentSeatOccupied >= 5):
                    data2[rowCount][colCount] = "L"
                    changeHappened += 1
                else:
                    data2[rowCount][colCount] = "#"
            if (data[rowCount][colCount] == "."):
                data2[rowCount][colCount] = "."
    return data2


def howManySeatsOccupied(data):
    count = 0
    for rowCount, row in enumerate(data):
        for colCount, seat in enumerate(row):
            if (data[rowCount][colCount] == "#"):
                count += 1
    return count


data = populateFromFile()
while(changeHappened != 0):
    data2 = processWaitingArea(data)
    data = data2

print("Part 1 - answer:", howManySeatsOccupied(data))

data = populateFromFile()
changeHappened = -1
while(changeHappened != 0):
    data2 = processWaitingArea2(data)
    data = data2

print("Part 2 - answer:", howManySeatsOccupied(data))
