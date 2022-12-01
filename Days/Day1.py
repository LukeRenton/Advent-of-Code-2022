tot = []
file = open("input.txt", "r")
calories = [line.strip() for line in file]
file.close()
acc = 0
for i in calories:
    if (i != ''):
        acc += int(i)
    else:
        tot.append(acc)
        acc = 0

tot.sort(reverse=True)
print("Max: ", tot[0])
print("Total 3: ",tot[0] + tot[1] +tot[2])

    