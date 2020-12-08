file1 = open('input7.txt', 'r')
Lines = file1.readlines()

bagsWithShinyGold = {}
totalNumOfBags = 0


def processBag(colour):
    for line in Lines:
        found = False
        numberOfInnerBags = 0
        splitContain = line.strip().split(' bags contain ')
        outerBag = splitContain[0]
        internalBagSplit = splitContain[1].split(',')
        # search for bag color
        if (splitContain[1].__contains__('shiny gold')):
            bagsWithShinyGold[outerBag] = 'Yes'
            found = True

        for innerBag in internalBagSplit:
            innerBag = innerBag.replace('.', '').replace(
                ' bag', '').replace(' bags', '').strip()
            innerBagSplit = innerBag.split(' ')
            if(innerBagSplit[0].strip() != 'no'):
                numberOfInnerBags += int(innerBagSplit[0].strip())
            innerBagSplit = innerBagSplit[1:]
            innerBag = ' '.join(innerBagSplit)
            # search for bag color
            tempBagsWithShinyGold = bagsWithShinyGold.copy()
            for bagColour in tempBagsWithShinyGold.keys():
                if (innerBag.__contains__(bagColour) and found == False):
                    bagsWithShinyGold[outerBag] = 'Yes'
                    found = True


# Part 1
for line in Lines:
    splitContain = line.strip().split(' bags contain ')
    outerBag = splitContain[0]
    processBag(outerBag)

print("Part 1 - Number of Bags that may contain other Shiny Gold Bags:",
      len(bagsWithShinyGold))


def howManyBagsWithin(colour, numOfBags):
    global totalNumOfBags
    for line in Lines:
        numberOfInnerBagsForOuter = 0
        splitContain = line.strip().split(' bags contain ')
        outerBag = splitContain[0]
        if (outerBag != colour):
            continue

        internalBagSplit = splitContain[1].split(',')

        for innerBag in internalBagSplit:
            numberOfInnerBags = 0
            innerBag = innerBag.replace('.', '').replace(
                ' bag', '').replace(' bags', '').strip()
            innerBagSplit = innerBag.split(' ')
            if(innerBagSplit[0].strip() != 'no'):
                numberOfInnerBags = int(innerBagSplit[0].strip())
                numberOfInnerBagsForOuter += numberOfInnerBags
                innerBagSplit = innerBagSplit[1:]
                innerBag = ' '.join(innerBagSplit)
                if innerBag[-1] == 's':
                    innerBag = innerBag[:-1]

                howManyBagsWithin(
                    innerBag, numberOfInnerBags * numOfBags)

        totalNumOfBags += numberOfInnerBagsForOuter*numOfBags


howManyBagsWithin('shiny gold', 1)
print("Part 2 - Number of Bags in a Shiny Gold Bag:", totalNumOfBags)
