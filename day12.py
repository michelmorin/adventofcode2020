file1 = open('input12.txt', 'r')
Lines = file1.readlines()


def populateFromFile():
    data = []
    for line in Lines:
        data.append(line.strip())
    return data


currentPointing = "E"
currentPositionHorizontal = 0
currentPositionVertical = 0

wayPointCurrentPointing = "E"
wayPointCurrentPositionHorizontal = 0
wayPointCurrentPositionVertical = 0


def process(data):
    global currentPointing
    global currentPositionHorizontal
    global currentPositionVertical

    for instruction in data:
        direction = instruction[0]
        byValue = int(instruction[1:])
        if(direction == "N"):
            currentPositionVertical += byValue
        if(direction == "S"):
            currentPositionVertical -= byValue
        if(direction == "E"):
            currentPositionHorizontal += byValue
        if(direction == "W"):
            currentPositionHorizontal -= byValue
        if(direction == "L"):
            if(currentPointing == "E" and byValue == 90):
                currentPointing = "N"
            elif(currentPointing == "E" and byValue == 180):
                currentPointing = "W"
            elif(currentPointing == "E" and byValue == 270):
                currentPointing = "S"

            elif(currentPointing == "W" and byValue == 90):
                currentPointing = "S"
            elif(currentPointing == "W" and byValue == 180):
                currentPointing = "E"
            elif(currentPointing == "W" and byValue == 270):
                currentPointing = "N"

            elif(currentPointing == "N" and byValue == 90):
                currentPointing = "W"
            elif(currentPointing == "N" and byValue == 180):
                currentPointing = "S"
            elif(currentPointing == "N" and byValue == 270):
                currentPointing = "E"

            elif(currentPointing == "S" and byValue == 90):
                currentPointing = "E"
            elif(currentPointing == "S" and byValue == 180):
                currentPointing = "N"
            elif(currentPointing == "S" and byValue == 270):
                currentPointing = "W"
        if(direction == "R"):
            if(currentPointing == "E" and byValue == 90):
                currentPointing = "S"
            elif(currentPointing == "E" and byValue == 180):
                currentPointing = "W"
            elif(currentPointing == "E" and byValue == 270):
                currentPointing = "N"

            elif(currentPointing == "W" and byValue == 90):
                currentPointing = "N"
            elif(currentPointing == "W" and byValue == 180):
                currentPointing = "E"
            elif(currentPointing == "W" and byValue == 270):
                currentPointing = "S"

            elif(currentPointing == "N" and byValue == 90):
                currentPointing = "E"
            elif(currentPointing == "N" and byValue == 180):
                currentPointing = "S"
            elif(currentPointing == "N" and byValue == 270):
                currentPointing = "W"

            elif(currentPointing == "S" and byValue == 90):
                currentPointing = "W"
            elif(currentPointing == "S" and byValue == 180):
                currentPointing = "N"
            elif(currentPointing == "S" and byValue == 270):
                currentPointing = "E"
        if(direction == "F"):
            if(currentPointing == "E"):
                currentPositionHorizontal += byValue
            elif(currentPointing == "W"):
                currentPositionHorizontal -= byValue
            elif(currentPointing == "N"):
                currentPositionVertical += byValue
            elif(currentPointing == "S"):
                currentPositionVertical -= byValue


def process2(data):
    global currentPointing
    global currentPositionHorizontal
    global currentPositionVertical
    global wayPointCurrentPointing
    global wayPointCurrentPositionHorizontal
    global wayPointCurrentPositionVertical

    for instruction in data:
        direction = instruction[0]
        byValue = int(instruction[1:])
        if(direction == "N"):
            wayPointCurrentPositionVertical += byValue
        if(direction == "S"):
            wayPointCurrentPositionVertical -= byValue
        if(direction == "E"):
            wayPointCurrentPositionHorizontal += byValue
        if(direction == "W"):
            wayPointCurrentPositionHorizontal -= byValue
        if(direction == "L"):
            if(byValue == 90):
                origWayPointCurrentPositionHorizontal = wayPointCurrentPositionHorizontal
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionHorizontal = int(
                        "-" + str(wayPointCurrentPositionVertical))
                # South
                else:
                    wayPointCurrentPositionHorizontal = int(
                        str(wayPointCurrentPositionVertical)[1:])
                # East
                if (origWayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionVertical = origWayPointCurrentPositionHorizontal
                # West
                else:
                    wayPointCurrentPositionVertical = origWayPointCurrentPositionHorizontal

            elif(byValue == 180):
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionVertical = int(
                        "-" + str(wayPointCurrentPositionVertical))
                # South
                else:
                    wayPointCurrentPositionVertical = int(
                        str(wayPointCurrentPositionVertical)[1:])
                # East
                if (wayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionHorizontal = int(
                        "-" + str(wayPointCurrentPositionHorizontal))
                # West
                else:
                    wayPointCurrentPositionHorizontal = int(
                        str(wayPointCurrentPositionHorizontal)[1:])
            elif(byValue == 270):
                origWayPointCurrentPositionHorizontal = wayPointCurrentPositionHorizontal
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionHorizontal = wayPointCurrentPositionVertical
                # South
                else:
                    wayPointCurrentPositionHorizontal = wayPointCurrentPositionVertical
                # East
                if (origWayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionVertical = int(
                        "-" + str(origWayPointCurrentPositionHorizontal))
                # West
                else:
                    wayPointCurrentPositionVertical = int(
                        str(origWayPointCurrentPositionHorizontal)[1:])
        if(direction == "R"):
            if(byValue == 90):
                origWayPointCurrentPositionHorizontal = wayPointCurrentPositionHorizontal
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionHorizontal = wayPointCurrentPositionVertical
                # South
                else:
                    wayPointCurrentPositionHorizontal = wayPointCurrentPositionVertical
                # East
                if (origWayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionVertical = int(
                        "-" + str(origWayPointCurrentPositionHorizontal))
                # West
                else:
                    wayPointCurrentPositionVertical = int(
                        str(origWayPointCurrentPositionHorizontal)[1:])

            elif(byValue == 180):
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionVertical = int(
                        "-" + str(wayPointCurrentPositionVertical))
                # South
                else:
                    wayPointCurrentPositionVertical = int(
                        str(wayPointCurrentPositionVertical)[1:])
                # East
                if (wayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionHorizontal = int(
                        "-" + str(wayPointCurrentPositionHorizontal))
                # West
                else:
                    wayPointCurrentPositionHorizontal = int(
                        str(wayPointCurrentPositionHorizontal)[1:])
            elif(byValue == 270):
                origWayPointCurrentPositionHorizontal = wayPointCurrentPositionHorizontal
                # North
                if (wayPointCurrentPositionVertical >= 0):
                    wayPointCurrentPositionHorizontal = int(
                        "-" + str(wayPointCurrentPositionVertical))
                # South
                else:
                    wayPointCurrentPositionHorizontal = int(
                        str(wayPointCurrentPositionVertical)[1:])
                # East
                if (origWayPointCurrentPositionHorizontal >= 0):
                    wayPointCurrentPositionVertical = origWayPointCurrentPositionHorizontal
                # West
                else:
                    wayPointCurrentPositionVertical = origWayPointCurrentPositionHorizontal

        if(direction == "F"):
            # Norths
            if (wayPointCurrentPositionVertical >= 0):
                movement = wayPointCurrentPositionVertical * byValue
                currentPositionVertical += movement
            # South
            else:
                movement = wayPointCurrentPositionVertical * byValue
                currentPositionVertical += movement
            # East
            if (wayPointCurrentPositionHorizontal >= 0):
                movement = wayPointCurrentPositionHorizontal * byValue
                currentPositionHorizontal += movement
            # West
            else:
                movement = wayPointCurrentPositionHorizontal * byValue
                currentPositionHorizontal += movement


def printLocation():
    global currentPointing
    global currentPositionHorizontal
    global currentPositionVertical
    global wayPointCurrentPointing
    global wayPointCurrentPositionHorizontal
    global wayPointCurrentPositionVertical

    print("Ship Location")
    if (currentPositionVertical > 0):
        print("North", currentPositionVertical)
    else:
        print("South", int(str(currentPositionVertical)[1:]))

    if (currentPositionHorizontal > 0):
        print("East", currentPositionHorizontal)
    else:
        print("West", int(str(currentPositionHorizontal)[1:]))

    print("Waypoint Location")
    if (wayPointCurrentPositionVertical > 0):
        print("North", wayPointCurrentPositionVertical)
    else:
        print("South", int(
            str(wayPointCurrentPositionVertical)[1:]))

    if (wayPointCurrentPositionHorizontal > 0):
        print("East", wayPointCurrentPositionHorizontal)
    else:
        print("West", int(
            str(wayPointCurrentPositionHorizontal)[1:]))


data = populateFromFile()
process(data)

print("Ship Location")
if (currentPositionVertical > 0):
    print("North", currentPositionVertical)
else:
    currentPositionVertical = int(str(currentPositionVertical)[1:])
    print("South", currentPositionVertical)

if (currentPositionHorizontal > 0):
    print("East", currentPositionHorizontal)
else:
    currentPositionHorizontal = int(str(currentPositionHorizontal)[1:])
    print("West", currentPositionHorizontal)

print("Part 1 - answer:", currentPositionVertical+currentPositionHorizontal)
print("------------------------------------")

currentPointing = "E"
currentPositionHorizontal = 0
currentPositionVertical = 0

wayPointCurrentPointing = "E"
wayPointCurrentPositionHorizontal = 10
wayPointCurrentPositionVertical = 1

process2(data)
# printLocation()
print("Ship Location")
if (currentPositionVertical > 0):
    print("North", currentPositionVertical)
else:
    currentPositionVertical = int(str(currentPositionVertical)[1:])
    print("South", currentPositionVertical)

if (currentPositionHorizontal > 0):
    print("East", currentPositionHorizontal)
else:
    currentPositionHorizontal = int(str(currentPositionHorizontal)[1:])
    print("West", currentPositionHorizontal)
print("Waypoint Location")
if (wayPointCurrentPositionVertical > 0):
    print("North", wayPointCurrentPositionVertical)
else:
    print("South", int(
        str(wayPointCurrentPositionVertical)[1:]))

if (wayPointCurrentPositionHorizontal > 0):
    print("East", wayPointCurrentPositionHorizontal)
else:
    print("West", int(
        str(wayPointCurrentPositionHorizontal)[1:]))
print("Part 2 - answer:", currentPositionVertical+currentPositionHorizontal)
