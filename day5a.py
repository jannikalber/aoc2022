import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

stacks = []


def move(from_, to):
	item = stacks[from_ - 1].pop()
	stacks[to - 1].append(item)


for i in file.readlines():
	i = i.replace("\n", "")
	if not i.startswith("move"):
		for j in range(0, len(i), 4):
			if len(stacks) < j // 4 + 1:
				stacks.append([])
			if i[j] == "[":
				stacks[j // 4].insert(0, i[j + 1])
	else:
		i = i.split(" ")
		for _ in range(int(i[1])):
			move(int(i[3]), int(i[5]))

for i in stacks:
	if len(i) > 0:
		print(i[len(i) - 1], end="")
print()
