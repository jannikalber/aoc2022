import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

mine = []
yours = []

for i in file.readlines():
	i = i.split(" ")
	if i[0] == "A":
		yours.append(1)
	elif i[0] == "B":
		yours.append(2)
	elif i[0] == "C":
		yours.append(3)
	
	if i[1].strip() == "X":
		mine.append(1)
	elif i[1].strip() == "Y":
		mine.append(2)
	elif i[1].strip() == "Z":
		mine.append(3)

assert len(mine) == len(yours)

score = 0

wins = [["u", "y", "m"], ["m", "u", "y"], ["y", "m", "u"]]

for i in range(len(mine)):
	winner = wins[mine[i] - 1][yours[i] - 1]
	score += mine[i]
	if winner == "m":
		score += 6
	elif winner == "u":
		score += 3

print(score)
