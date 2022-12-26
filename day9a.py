import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

position = set()
x = 0
y = 0

x_tail = 0
y_tail = 0

for i in file.readlines():
	i = i.split(" ")
	pos = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}[i[0]]
	for j in range(int(i[1])):
		x += pos[0]
		y += pos[1]
		
		if (x - x_tail) ** 2 + (y - y_tail) ** 2 > 2:
			if abs(pos[0]) > 0:
				x_tail = x - pos[0]
				y_tail = y
			elif abs(pos[1]) > 0:
				x_tail = x
				y_tail = y - pos[1]
		
		position.add(str([x_tail, y_tail]))

print(len(position))
