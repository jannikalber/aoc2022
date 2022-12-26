import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

chamber = []

for i in range(150):
	chamber.append(7 * ["."])


def ausgabe():
	for i in chamber[:15]:
		print("".join(i))


topest = 0
shapei = 0
patterni = 0

pattern = file.read().strip()
shapes = [["####"], [".#.", "###", ".#."], ["..#", "..#", "###"], ["#", "#", "#", "#"], ["##", "##"]]

for _ in range(2022):
	shape = shapes[shapei]
	y = topest + 5
	x = 2
	
	if y + len(shape) - 1 > len(chamber):
		for _ in range(y + len(shape) - 1 - len(chamber)):
			chamber.insert(0, 7 * ["."])
	
	ok = True
	while ok:
		for mover in [[-1, 0], "i"]:
			if not ok:
				continue
			if mover == "i":
				mover = pattern[patterni]
				if mover == ">":
					mover = [0, 1]
				else:
					mover = [0, -1]
				patterni = (patterni + 1) % len(pattern)
			
			# Jetzetle
			try:
				for add_y in range(len(shape) - 1, -1, -1):
					for add_x in range(len(shape[0])):
						if shape[len(shape) - 1 - add_y][add_x] == "#":
							target_x = x + add_x + mover[1]
							target_y = y + add_y + mover[0]
							
							if target_y < 1 or (0 <= target_x < 7 and chamber[-target_y][target_x] == "#" and mover[1] == 0):
								ok = False
								raise TimeoutError()
							
							if not 0 <= target_x < 7 or chamber[-(target_y)][target_x] == "#":
								raise TimeoutError()
				
				x += mover[1]
				y += mover[0]
			except TimeoutError:
				pass
	
	# Position it
	for add_y in range(len(shape) - 1, -1, -1):
		for add_x in range(len(shape[0])):
			if shape[len(shape) - 1 - add_y][add_x] == "#":
				chamber[-(y + add_y)][x + add_x] = "#"
	topestl = y + len(shape) - 1
	if topestl > topest:
		topest = topestl
	shapei = (shapei + 1) % len(shapes)

ausgabe()
print(7 * "v")

print()
print(topest)
