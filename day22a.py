import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

content = file.read().split("\n\n")
field = content[0].split("\n")
code = content[1].strip()

lengths = [len(x) for x in field]
maxl = max(lengths)

for i in range(len(field)):
	if len(field[i]) < maxl:
		for _ in range(maxl - len(field[i])):
			field[i] += " "



def find_point(direction, where):
	if direction % 2 == 0:
		start = 0
		change = 1
		if direction == 2:
			change = -1
			start = len(field[where]) - 1
		for _ in range(len(field[where])):
			if field[where][start] != " ":
				break
			start += change
		return [start, where]
	else:
		start = 0
		change = 1
		if direction == 3:
			change = -1
			start = len(field) - 1
		for _ in range(len(field)):
			if field[start][where] != " ":
				break
			start += change
		return [where, start]


direction = 0
pos = find_point(direction, 0)
current_num = ""
for ii in range(len(code)):
	i = code[ii]
	if i.isnumeric():
		current_num += i
		
		if ii >= len(code) - 1 or not code[ii + 1].isnumeric():
			directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
			for _ in range(int(current_num)):
				d = directions[direction]
				
				newpoint = pos[:]
				for x in range(2):
					newpoint[x] += d[x]
				
				keyerror = False
				try:
					field[newpoint[1]][newpoint[0]]
				except IndexError:
					keyerror = True
				
				if keyerror or field[newpoint[1]][newpoint[0]] == " ":
					newpoint = find_point(direction, newpoint[0] if newpoint[0] == pos[0] else newpoint[1])
				
				if field[newpoint[1]][newpoint[0]] != "#":
					pos = newpoint[:]
				else:
					break
			
			current_num = ""
	else:
		turns = 1 if i == "R" else -1
		direction = (direction + turns) % 4

print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + direction)
