import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

elves = {}
name = 0
field = [x.strip() for x in file.readlines()]
for y in range(len(field)):
	for x in range(len(field[0])):
		if field[y][x] == "#":
			elves[name] = [x, y]
			name += 1


def create_map():
	x_coords = [x[0] for x in elves.values()]
	y_coords = [x[1] for x in elves.values()]
	
	min_x = min(x_coords)
	min_y = min(y_coords)
	max_x = max(x_coords)
	max_y = max(y_coords)
	
	map = []
	for _ in range(max_y - min_y + 1):
		substr = []
		for _ in range(max_x - min_x + 1):
			substr.append(".")
		map.append(substr)
	
	for i in elves.values():
		map[i[1] - min_y][i[0] - min_x] = "#"
	
	return map


def ausgabe():
	map = create_map()
	for i in map:
		for j in i:
			print(j, end="")
		print()
	
	print()


# Rounds
priorities = ["north", "south", "west", "east"]
positions_to_check = {"north": [[x, -1] for x in [0, 1, -1]], "south": [[x, 1] for x in [0, 1, -1]],
                      "west": [[-1, x] for x in [0, 1, -1]], "east": [[1, x] for x in [0, 1, -1]]}
velocities = {"north": [0, -1], "south": [0, 1], "east": [1, 0], "west": [-1, 0]}
for round in range(10):
	new_elves = {}
	for elve in range(name):
		pr_start = round % 4
		directions = []
		for i in range(4):
			direction = priorities[pr_start]
			
			okay = True
			for pos in positions_to_check[direction]:
				pos2 = elves[elve][:]
				for x in range(2):
					pos2[x] += pos[x]
				if pos2 in elves.values():
					okay = False
					break
			
			if okay:
				directions.append(direction)
			
			pr_start = (pr_start + 1) % 4
		
		if 0 < len(directions) < 4:
			direction = directions.pop(0)
			new_pos = elves[elve][:]
			for x in range(2):
				new_pos[x] += velocities[direction][x]
			new_elves[elve] = new_pos
		else:
			new_elves[elve] = elves[elve][:]
	
	# Finally move the elves
	for elve in range(name):
		new_pos = new_elves[elve]
		
		new_pos_count = list(new_elves.values()).count(new_pos)
		if new_pos_count == 1:
			elves[elve] = new_pos

single_line_map = []
for i in create_map():
	for j in i:
		single_line_map.append(j)
print(single_line_map.count("."))
