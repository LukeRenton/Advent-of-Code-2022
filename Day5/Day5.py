import os
import re
import copy

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(location,'input.txt')) as file:
       lines = [line for line in file]

spacing = int(len(lines[0])/4)
stacks = []
for i in range(spacing):
    lane = []
    for j in range(spacing-1):
        element = lines[j][i*4:i*4+4].strip()
        if (element != ''):
            lane.append(element)
    stacks.append(lane[::-1])

def part_1(lines, stacks):
    for i in range(spacing+1, len(lines)):
        order = [int(s) for s in re.findall(r'\b\d+\b', lines[i])]
        for j in range(order[0]):
            stacks[order[2]-1].append(stacks[order[1]-1].pop())

    result_1 = ""
    for i in range(spacing):
        result_1 += stacks[i][-1].replace("[", "").replace("]","")
    return result_1

def part_2(lines, stacks):
    for i in range(spacing+1, len(lines)):
        order = [int(s) for s in re.findall(r'\b\d+\b', lines[i])]
        clump = []
        for j in range(order[0]):
            clump.append(stacks[order[1]-1].pop())
        clump=clump[::-1]
        for j in range(len(clump)):
            stacks[order[2]-1].append(clump[j])
    result_2 = ""
    for i in range(spacing):
        result_2 += stacks[i][-1].replace("[", "").replace("]","")
    return result_2

stacks_1 = copy.deepcopy(stacks)
stacks_2 = copy.deepcopy(stacks)
print("PART 1:", part_1(lines, stacks_1))
print("PART 2:", part_2(lines, stacks_2))