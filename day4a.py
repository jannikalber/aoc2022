import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

counter = 0

for i in file.readlines():
	i = i.split(",")
	f = i[0].split("-")
	s = i[1].split("-")
	
	area1 = set(range(int(f[0]), int(f[1]) + 1))
	area2 = set(range(int(s[0]), int(s[1]) + 1))
	
	if area1.issubset(area2) or area2.issubset(area1):
		counter += 1

print(counter)
