import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

sensors = []
beacons = []

for i in file.readlines():
	i = i.replace(",", "").replace(":", "").split(" ")
	x = int(i[2].split("=")[1])
	y = int(i[3].split("=")[1])
	xb = int(i[-2].split("=")[1])
	yb = int(i[-1].split("=")[1])
	
	man = abs(x - xb) + abs(y - yb)
	
	sensors.append({"x": x, "y": y, "xb": xb, "yb": yb, "man": man})
	beacons.append([xb, yb])

mm = max([x["man"] for x in sensors])
mix = min([x["x"] for x in sensors])
mx = max([x["x"] for x in sensors])

count = 0
for x in range(mix - mm - 50, mx + mm + 50):
	y = 2000000
	
	if [x, y] in beacons:
		continue
	
	for s in sensors:
		man = abs(s["x"] - x) + abs(s["y"] - y)
		if man <= s["man"]:
			count += 1
			break

print(count)
