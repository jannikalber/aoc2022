import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

trees = []
for i in file.readlines():
	trees.append([int(x) for x in i.strip()])
visible = set()

for i in range(len(trees[0])):
	cnt = -1
	for j in range(len(trees)):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
			cnt = val

for j in range(len(trees)):
	cnt = -1
	for i in range(len(trees[0])):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
			cnt = val

for j in range(len(trees)):
	cnt = -1
	for i in range(len(trees[0]) - 1, -1, -1):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
			cnt = val

for i in range(len(trees[0])):
	cnt = -1
	for j in range(len(trees) - 1, -1, -1):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
			cnt = val

print(len(visible))
