file1 = open('input8.txt', 'r')
Lines = file1.readlines()

completedFullInstruction = False


def populateOriginalFile():
    instructions = []
    for line in Lines:
        instructions.append(line.strip().split(' '))
    return instructions


def hasInstructionBeenExecutedBefore(instNumber, executedInstruction):
    if executedInstruction.get(instNumber):
        return True
    else:
        executedInstruction[instNumber] = "yes"
        return False


def runInstructionSet(instructionsLocal, changedLine, changeInstruction):
    global completedFullInstruction
    accumulator = 0
    currentInstructionLocation = 0
    executedInstruction = {}

    if(changeInstruction):
        if (instructionsLocal[changedLine][0] == 'nop'):
            instructionsLocal[changedLine][0] = 'jmp'
        else:
            if (instructionsLocal[changedLine][0] == 'jmp'):
                instructionsLocal[changedLine][0] = 'nop'

    # Let's process the instructions
    while (not hasInstructionBeenExecutedBefore(currentInstructionLocation, executedInstruction)):
        # nop stands for No Operation - it does nothing. The instruction immediately below it is executed next.
        if (instructionsLocal[currentInstructionLocation][0] == 'nop'):
            currentInstructionLocation += 1
            if(currentInstructionLocation == len(instructionsLocal)):
                completedFullInstruction = True
                return accumulator
            continue

        # acc increases or decreases a single global value called the accumulator by the value given in the argument.
        # For example, acc +7 would increase the accumulator by 7. The accumulator starts at 0.
        # After an acc instruction, the instruction immediately below it is executed next.
        if (instructionsLocal[currentInstructionLocation][0] == 'acc'):
            accumulator += int(
                instructionsLocal[currentInstructionLocation][1])
            currentInstructionLocation += 1
            if(currentInstructionLocation == len(instructionsLocal)):
                completedFullInstruction = True
                return accumulator

            # print(previousInstructionLocation, "next is", instructions[currentInstructionLocation])
            continue

        # jmp jumps to a new instruction relative to itself. The next instruction to execute is found using the
        # argument as an offset from the jmp instruction; for example, jmp +2 would skip the next instruction,
        # jmp +1 would continue to the instruction immediately below it, and jmp -20 would cause the instruction
        # 20 lines above to be executed next.
        if (instructionsLocal[currentInstructionLocation][0] == 'jmp'):
            currentInstructionLocation += int(
                instructionsLocal[currentInstructionLocation][1])
            if(currentInstructionLocation == len(instructionsLocal)):
                completedFullInstruction = True
                return accumulator
            continue

    return accumulator


accumulator = runInstructionSet(populateOriginalFile(), 0, False)
print("Part 1 - accumulator:", accumulator)

# Part 2, gonna try every combination changing code and see until found
count = 0
accumulator = 0
for line in Lines:
    if (completedFullInstruction == False):
        accumulator = runInstructionSet(populateOriginalFile(), count, True)
        count += 1
    else:
        break

print("Part 2 - accumulator:", accumulator)
