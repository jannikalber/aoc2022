import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

counter = 0

for i in file.readlines():
	i = i.split(",")
	f = i[0].split("-")
	s = i[1].split("-")
	
	area1 = range(int(f[0]), int(f[1]) + 1)
	area2 = range(int(s[0]), int(s[1]) + 1)
	
	intersection = [value for value in area1 if value in area2]
	if len(intersection) >= 1:
		counter += 1

print(counter)
