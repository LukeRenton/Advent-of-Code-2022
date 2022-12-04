import os
import re

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(location,'input.txt')) as file:
        sections = [map(int, re.split(",|-", line)) for line in file]

sections = [((a, b), (c, d)) for a, b, c, d in sections]
def overlap_1(s1, s2):
    if (s1[0] <= s2[0] and s1[1] >= s2[1]) or (s1[0] >= s2[0] and s1[1] <= s2[1]):
        return 1
    return 0

def overlap_2(s1, s2):
    s1 = [i for i in range(s1[0],s1[1]+1)]
    s2 = [i for i in range(s2[0],s2[1]+1)]
    overlap = set(s1) & set(s2)
    if len(overlap):
        return 1
    return 0

pairs_count_1 = 0
pairs_count_2 = 0
for i in range(len(sections)):
    pairs_count_1 += overlap_1(sections[i][0],sections[i][1])
    pairs_count_2 += overlap_2(sections[i][0],sections[i][1])
print("PART 1: ",pairs_count_1)
print("PART 2: ",pairs_count_2)