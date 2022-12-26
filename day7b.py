import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

input = file.readlines()
pwd = "/"

sizes = {}

while len(input) > 0:
	instr = input.pop(0)
	if instr.startswith("$ "):
		instr = instr.strip().split(" ")
		
		cmd = instr[1]
		if cmd == "cd":
			param = instr[2]
			if param == "/":
				pwd = "/"
			elif param == "..":
				pwd = "/".join(pwd.split("/")[:-2]) + "/"
			else:
				pwd += param + "/"
		
		elif cmd == "ls":
			sum_ = 0
			while len(input) > 0 and not input[0].startswith("$ "):
				s = input.pop(0).split(" ")
				if s[0] != "dir":
					sum_ += int(s[0])
			sizes[pwd] = sum_

sizes2 = {}
for j in sizes.keys():
	sizes2s = 0
	for k in sizes.keys():
		if k.startswith(j):
			sizes2s += sizes[k]
	sizes2[j] = sizes2s

space_to_free = 30000000 - (70000000 - sizes2["/"])

winner = []
for i in sizes2.keys():
	if sizes2[i] >= space_to_free and (len(winner) == 0 or winner[1] > sizes2[i]):
		winner = [i, sizes2[i]]

print(winner[1])
