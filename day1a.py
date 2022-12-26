import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

reindeers = file.read().strip().split("\n\n")
cals = []

for i in reindeers:
	cals.append(sum([int(x) for x in i.split("\n")]))

print(max(cals))
