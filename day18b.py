import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

cubes = []
for i in file.readlines():
	cubes.append([int(x) for x in i.split(",")])

mins = [min([x[0] for x in cubes]) - 1, min([x[1] for x in cubes]) - 1, min([x[2] for x in cubes]) - 1]
maxs = [max([x[0] for x in cubes]) + 1, max([x[1] for x in cubes]) + 1, max([x[2] for x in cubes]) + 1]

visited = set()
found = set()

nexts = [[mins[0], mins[1], mins[2]]]
visited.add(str(nexts[0]))

while len(nexts) > 0:
	st = nexts.pop(0)
	assert st not in cubes
	
	for x in range(len(st)):
		for l in [-1, 1]:
			newp = st[:]
			newp[x] += l
			
			if str(newp) not in visited and newp[0] <= maxs[0] and newp[1] <= maxs[1] and newp[2] <= maxs[2] and newp[
				0] >= mins[0] and newp[1] >= mins[1] and newp[2] >= mins[2]:
				if newp in cubes:
					found.add(str(newp) + " " + str(l) + " " + str(x))
				else:
					visited.add(str(newp))
					nexts.append(newp)

print(len(found))
