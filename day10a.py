import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")
cnt = file.readlines()

todo = {0: 0}
strengths = []
X = 1
additional = 1


def check():
	if cycle in range(20, 221, 40):
		strengths.append(cycle * X)


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

assert len(strengths) == 6
print(sum(strengths))
