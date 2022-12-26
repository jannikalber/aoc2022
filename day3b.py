import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

counter = 0

content = file.readlines()
for i in range(0, len(content), 3):
	first = content[i].strip()
	second = content[i + 1].strip()
	third = content[i + 2].strip()
	intersection = list(set([value for value in first if value in second and value in third]))
	double = intersection[0]
	if double.islower():
		counter += ord(double) - 96
	else:
		counter += ord(double) - 65 + 27

print(counter)
