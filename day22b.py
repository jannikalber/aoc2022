import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

content = file.read().split("\n\n")
pre_field = content[0].split("\n")
code = content[1].strip()

lengths = [len(x) for x in pre_field]
max_length = max(lengths)
for i in range(len(pre_field)):
	if len(pre_field[i]) < max_length:
		for _ in range(max_length - len(pre_field[i])):
			pre_field[i] += " "

fields_size = 50
fields = []
for i in range(len(pre_field) // fields_size):
	i *= fields_size
	for j in range(len(pre_field[0]) // fields_size):
		j *= fields_size
		if pre_field[i][j] != " ":
			subfield = []
			array_cpy = pre_field[i:i + fields_size]
			for k in array_cpy:
				subfield.append(k[j:j + fields_size])
			fields.append(subfield)

# These are the transitions for the given net. They don't work for every net.
# [new_field, invertX, invertY, Change, Direction
transitions = {0: {"^": [5, False, False, True, 1], "v": [2, False, True, False, 0], ">": [1, True, False, False, 0],
                   "<": [3, False, True, False, 2]},
               1: {"^": [5, False, True, False, 0], "v": [2, False, False, True, 1], ">": [4, False, True, False, 2],
                   "<": [0, True, False, False, 0]},
               2: {"^": [0, False, True, False, 0], "v": [4, False, True, False, 0], ">": [1, False, False, True, -1],
                   "<": [3, False, False, True, -1]},
               3: {"^": [2, False, False, True, 1], "v": [5, False, True, False, 0], ">": [4, True, False, False, 0],
                   "<": [0, False, True, False, 2]},
               4: {"^": [2, False, True, False, 0], "v": [5, False, False, True, 1], ">": [1, False, True, False, 2],
                   "<": [3, True, False, False, 0]},
               5: {"^": [3, False, True, False, 0], "v": [1, False, True, False, 0], ">": [4, False, False, True, -1],
                   "<": [0, False, False, True, -1]}}


def find_point():
	global direction, field_index, field, pos
	direction_dictonary = {0: ">", 1: "v", 2: "<", 3: "^"}
	trans = transitions[field_index][direction_dictonary[direction]]
	new_x = fields_size - 1 - pos[0] if trans[1] else pos[0]
	new_y = fields_size - 1 - pos[1] if trans[2] else pos[1]
	new_pos = [new_x, new_y] if not trans[3] else [new_y, new_x]
	new_direction = (direction + trans[4]) % 4
	return [trans[0], new_pos, new_direction]


direction = 0
field_index = 0
field = fields[field_index]
pos = [0, 0]
# code = "200"
current_num = ""
for ii in range(len(code)):
	i = code[ii]
	if i.isnumeric():
		current_num += i
		
		if ii >= len(code) - 1 or not code[ii + 1].isnumeric():
			directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
			for _ in range(int(current_num)):
				d = directions[direction]
				
				new_point = pos[:]
				for x in range(2):
					new_point[x] += d[x]
				
				keyerror = new_point[0] < 0 or new_point[1] < 0
				try:
					field[new_point[1]][new_point[0]]
				except IndexError:
					keyerror = True
				
				new_field_index = field_index
				new_direction = direction
				if keyerror:
					new_data = find_point()
					new_field_index = new_data[0]
					new_point = new_data[1]
					new_direction = new_data[2]
				
				if fields[new_field_index][new_point[1]][new_point[0]] != "#":
					field_index = new_field_index
					field = fields[field_index]
					direction = new_direction
					pos = new_point[:]
				else:
					break
			
			current_num = ""
	else:
		turns = 1 if i == "R" else -1
		direction = (direction + turns) % 4

global_position = [[1, 0], [2, 0], [1, 1], [0, 2], [1, 2], [0, 3]][field_index]
print(1000 * (pos[1] + global_position[1] * fields_size + 1) + 4 * (
		pos[0] + global_position[0] * fields_size + 1) + direction)
