import os

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
lines = open(os.path.join(location,'input.txt'), 'r')
moves = lines.read().upper().replace(' ','').split()
lines.close()

def point_move(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    if move == "Z":
        return 3

def point_win(p1, p2):
    if (chr(ord(p1) + (ord("X") -ord("A"))) == p2):
        return 3
    if ((p1 == "A" and p2 == "Y") or (p1 == "B" and p2 == "Z") or (p1 == "C" and p2 == "X")):
        return 6
    else:
        return 0

def find_move(p1,result):
    if (result == "X"):
        return chr(ord("A") + (ord(p1) - ord("A")+2)%3 + ord("X")-ord("A")) 
    if (result == "Y"):
        return chr(ord(p1) + (ord("X") -ord("A")))
    if (result == "Z"):
        return chr(ord("A") + (ord(p1) - ord("A")+1)%3 + ord("X")-ord("A"))

score_1 = 0
score_2 = 0
for i in moves:
    score_1 += point_win(i[0], i[1]) + point_move(i[1])
    move_2 = find_move(i[0], i[1])
    score_2 += point_win(i[0], move_2) + point_move(move_2)
print("PART ONE: ",score_1)
print("PART TWO: ", score_2)

