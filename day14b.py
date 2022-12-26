import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

points = []

for i in file.readlines():
	i = i.split(" -> ")
	
	point = None
	
	ok = False
	for j in i:
		if point is None:
			point = [int(x) for x in j.split(",")]
		else:
			ok = True
			point2 = [int(x) for x in j.split(",")]
			if point[0] == point2[0]:
				x = [point2[0]]
				y = range(min(point[1], point2[1]), max(point[1], point2[1]) + 1)
			elif point[1] == point2[1]:
				y = [point[1]]
				x = range(min(point[0], point2[0]), max(point[0], point2[0]) + 1)
			else:
				print("!")
			
			point = point2
			
			for ix in x:
				for iy in y:
					points.append([ix, iy])
	
	assert ok

x_min = min(x[0] for x in points)
x_max = max(max(x[0] for x in points), 500)
y_max = max(x[1] for x in points) + 1

view = []
for i in range(y_max + 1):
	x = []
	for i in range(x_max - x_min + 1):
		x.append(".")
	view.append(x)

x = []
for i in range(x_max - x_min + 1):
	x.append("#")
view.append(x)

for i in points:
	view[i[1]][i[0] - x_min] = "#"


def ausgabe():
	for i in view:
		print("".join(i))


def require(upper, x):
	global view, x_max, x_min
	if upper and x > x_max:
		for _ in range(x_max, x):
			for i in range(len(view)):
				view[i].append(".")
			view[i][-1] = "#"
		x_max = x
	
	elif not upper and x < x_min:
		for _ in range(x, x_min):
			for i in range(len(view)):
				view[i].insert(0, ".")
			view[i][0] = "#"
		x_min = x


count = 0
while view[0][500 - x_min] == ".":
	sand = [500, 0]
	
	moved = True
	while moved:
		i = sand
		require(True, i[0] + 1)
		require(False, i[0] - 1)
		if view[i[1] + 1][i[0] - x_min] == ".":
			sand = [sand[0], sand[1] + 1]
		elif view[i[1] + 1][i[0] - x_min - 1] == ".":
			sand = [sand[0] - 1, sand[1] + 1]
		elif view[i[1] + 1][i[0] - x_min + 1] == ".":
			sand = [sand[0] + 1, sand[1] + 1]
		else:
			moved = False
	
	count += 1
	
	view[sand[1]][sand[0] - x_min] = "o"

ausgabe()
print(count)
