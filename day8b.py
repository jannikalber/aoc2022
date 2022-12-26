import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

trees = []
for i in file.readlines():
	trees.append([int(x) for x in i.strip()])
visible = set()

scores = {}

for i in range(len(trees[0])):
	cnt = -1
	scenic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for j in range(len(trees)):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
		for p in range(cnt + 1):
			scenic[p] = 1
		cnt = val
		
		if str([j, i]) in scores:
			scores[str([j, i])].append(scenic[val])
		else:
			scores[str([j, i])] = [scenic[val]]
		for p in range(10):
			scenic[p] += 1

for j in range(len(trees)):
	cnt = -1
	scenic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(trees[0])):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
		for p in range(cnt + 1):
			scenic[p] = 1
		cnt = val
		
		if str([j, i]) in scores:
			scores[str([j, i])].append(scenic[val])
		else:
			scores[str([j, i])] = [scenic[val]]
		for p in range(10):
			scenic[p] += 1

for j in range(len(trees)):
	cnt = -1
	scenic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(trees[0]) - 1, -1, -1):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
		for p in range(cnt + 1):
			scenic[p] = 1
		cnt = val
		
		if str([j, i]) in scores:
			scores[str([j, i])].append(scenic[val])
		else:
			scores[str([j, i])] = [scenic[val]]
		for p in range(10):
			scenic[p] += 1

for i in range(len(trees[0])):
	cnt = -1
	scenic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for j in range(len(trees) - 1, -1, -1):
		val = trees[j][i]
		if val > cnt:
			visible.add(str([j, i]))
		for p in range(cnt + 1):
			scenic[p] = 1
		cnt = val
		
		if str([j, i]) in scores:
			scores[str([j, i])].append(scenic[val])
		else:
			scores[str([j, i])] = [scenic[val]]
		for p in range(10):
			scenic[p] += 1

ls = []
for i in scores.values():
	j = 1
	for k in i:
		j *= k
	
	ls.append(j)

print(max(ls))
