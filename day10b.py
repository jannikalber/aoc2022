import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")
cnt = file.readlines()

todo = {0: 0}
X = 1
additional = 1
current_pos = 0
row = ""
rows = []


def check():
	global rows, row, current_pos
	if current_pos == X - 1 or current_pos == X or current_pos == X + 1:
		row += "#"
	else:
		row += "."
	
	if current_pos + 1 in range(40, 241, 40):
		rows.append(row)
		row = ""
		current_pos = 0
	else:
		current_pos += 1


for i in range(len(cnt)):
	cycle = i + additional
	
	instr = cnt[i]
	instr = instr.split(" ")
	if instr[0] == "addx":
		check()
		additional += 1
		cycle += 1
		
		todo[cycle] = int(instr[1])
	
	check()
	
	# Update at the end
	if cycle in todo:
		X += todo[cycle]

print("\n".join(rows))
