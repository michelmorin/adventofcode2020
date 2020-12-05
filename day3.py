file1 = open('input3.txt', 'r')
Lines = file1.readlines()

w, h = 31, 323
array = [[0 for x in range(w)] for y in range(h)]

lineCount = 0
for line in Lines:
    charCount = 0
    line = line.strip()
    for charCount, char in enumerate(line):
        array[lineCount][charCount] = char
    lineCount += 1

numTrees1 = 0
linePOS = 0
charPOS = 0

while(linePOS < h-1):
    charPOS += 1
    linePOS += 1
    if (charPOS > w - 1):
        charPOS = charPOS - w
    if (array[linePOS][charPOS] == '#'):
        numTrees1 += 1

print("number of trees hit - Right 1, down 1:", numTrees1)

numTrees2 = 0
linePOS = 0
charPOS = 0

while(linePOS < h-1):
    charPOS += 3
    linePOS += 1
    if (charPOS > w - 1):
        charPOS = charPOS - w
    if (array[linePOS][charPOS] == '#'):
        numTrees2 += 1

print("Part 1 answer: number of trees hit - Right 3, down 1:", numTrees2)

numTrees3 = 0
linePOS = 0
charPOS = 0

while(linePOS < h-1):
    charPOS += 5
    linePOS += 1
    if (charPOS > w - 1):
        charPOS = charPOS - w
    if (array[linePOS][charPOS] == '#'):
        numTrees3 += 1

print("number of trees hit - Right 5, down 1:", numTrees3)

numTrees4 = 0
linePOS = 0
charPOS = 0

while(linePOS < h-1):
    charPOS += 7
    linePOS += 1
    if (charPOS > w - 1):
        charPOS = charPOS - w
    if (array[linePOS][charPOS] == '#'):
        numTrees4 += 1

print("number of trees hit - Right 7, down 1:", numTrees4)

numTrees5 = 0
linePOS = 0
charPOS = 0

while(linePOS < h-1):
    charPOS += 1
    linePOS += 2
    if (charPOS > w - 1):
        charPOS = charPOS - w
    if (array[linePOS][charPOS] == '#'):
        numTrees5 += 1

print("number of trees hit - Right 1, down 2:", numTrees5)

print("Part 2 answer:", numTrees1 *
      numTrees2 * numTrees3 * numTrees4 * numTrees5)
