import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

what_to_do = []
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
		what_to_do.append(0)
	elif i[1].strip() == "Y":
		what_to_do.append(1)
	elif i[1].strip() == "Z":
		what_to_do.append(2)

assert len(what_to_do) == len(yours)

score = 0

symbols = ["A", "B", "C"]
wins = [["u", "y", "m"], ["m", "u", "y"], ["y", "m", "u"]]
how_to_win = [[2, 0, 1], [0, 1, 2], [1, 2, 0]]

for i in range(len(what_to_do)):
	mine = how_to_win[what_to_do[i]][yours[i] - 1]
	winner = wins[mine][yours[i] - 1]
	score += mine + 1
	if winner == "m":
		score += 6
	elif winner == "u":
		score += 3

print(score)
