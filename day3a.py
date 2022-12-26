import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

counter = 0

for i in file.readlines():
	i = i.strip()
	first = i[:len(i) // 2]
	second = i[len(i) // 2:]
	intersection = list(set([value for value in first if value in second]))
	double = intersection[0]
	if double.islower():
		counter += ord(double) - 96
	else:
		counter += ord(double) - 65 + 27

print(counter)
