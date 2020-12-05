def highest(arr):
    max = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max


file1 = open('input5.txt', 'r')
Lines = file1.readlines()

arrayID = []
columns, rows = 8, 128
seatArray = [[0 for x in range(columns)] for y in range(rows)]

# initialize seats with 0
for r in range(rows):
    for c in range(columns):
        seatArray[r][c] = 'O'

for line in Lines:
    row = 0
    col = 0
    rowDirections = line[0:6]
    colDirections = line[7:10]

    rowMin = 0
    rowMax = 127
    for rowDirection in rowDirections:
        if (rowDirection == 'F'):
            rowMax = round((rowMin+rowMax)/2) - 1
        else:
            rowMin = round((rowMin+rowMax)/2)

    if (line[6] == 'F'):
        row = rowMin
    else:
        row = rowMax

    colMin = 0
    colMax = 7
    for colDirection in colDirections:
        if (colDirection == 'L'):
            colMax = round((colMin+colMax)/2) - 1
        else:
            colMin = round((colMin+colMax)/2)

    if (line[9] == 'L'):
        col = colMin
    else:
        col = colMax

    seatID = (row*8) + col
    arrayID.insert(1, seatID)
    seatArray[row][col] = "X"

myRow = 0
myCol = 0
for r in range(rows):
    print(seatArray[r][1], seatArray[r][2], seatArray[r][3], seatArray[r]
          [4], seatArray[r][5], seatArray[r][6], seatArray[r][7])
    for c in range(columns):
        if (seatArray[r][c] == 'O'):
            if (r > 1 and r < 122):
                myRow = r
                myCol = c

print("Highest Seat ID is", highest(arrayID))
print("Your Row is", myRow, "your Column is", myCol)
print("Your Seat ID is", (myRow*8)+myCol)
