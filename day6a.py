import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

file = file.read().strip()

for i in range(len(file) - 4):
	crnt = file[i:i + 4]
	ok = True
	for ji in range(len(crnt)):
		j = crnt[ji]
		if crnt.count(j) > 1:
			ok = False
	
	if ok:
		print(i + 4)
		break
