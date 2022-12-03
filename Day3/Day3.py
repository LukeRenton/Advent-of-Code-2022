import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = open(os.path.join(location,'input.txt'), 'r')
letters = lines.read().split()
lines.close()

def repeat_1(first, second):
    result = ""
    for i in first:
        if i in second and i not in result:
            result += i
    return result

def repeat_2(first, second, third):
    result = ""
    for i in first:
        if i in second and i in third and i not in result:
            result += i
    return result

def value(word):
    total = 0
    for i in word:
        if i.islower():
            total += ord(i) - ord("a") + 1
        else:
            total += ord(i) - ord("A") + 27
    return total

acc_1 = 0
for items in letters:
    rucksack_1, rucksack_2 = items[:len(items)//2], items[len(items)//2:]
    acc_1 += value(repeat_1(rucksack_1, rucksack_2))

acc_2 = 0
for i in range(0,len(letters),3):
    acc_2 += value(repeat_2(letters[i],letters[i+1],letters[i+2]))
    

print("PART 1: ", acc_1)
print("PART 2: ", acc_2)