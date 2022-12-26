import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

cubes = []
for i in file.readlines():
	cubes.append([int(x) for x in i.split(",")])

all = 0

for i in cubes:
	count = 6
	for j in cubes:
		if i != j:
			dis = sum([(i[x] - j[x])**2 for x in range(len(i))])
			
			if dis == 1:
				count -= 1
				
	all += count
	
print(all)
