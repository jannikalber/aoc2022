import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

sensors = []
limit = 4000000

for i in file.readlines():
	i = i.replace(",", "").replace(":", "").split(" ")
	x = int(i[2].split("=")[1])
	y = int(i[3].split("=")[1])
	xb = int(i[-2].split("=")[1])
	yb = int(i[-1].split("=")[1])
	
	man = abs(x - xb) + abs(y - yb)
	
	sensors.append({"x": x, "y": y, "xb": xb, "yb": yb, "man": man})

try:
	for i in range(limit + 1):
		gray_areas = {}
		for s in sensors:
			far_left = s["x"] - s["man"] + abs(s["y"] - i)
			far_right = s["x"] + s["man"] - abs(s["y"] - i)
			
			if far_left <= far_right:
				if (far_left not in gray_areas) or gray_areas[far_left] < far_right:
					gray_areas[far_left] = far_right
		
		starts = sorted(gray_areas.keys())
		x = 0
		while x <= limit:
			dests = []
			for k in starts:
				if k <= x <= gray_areas[k]:
					dests.append(gray_areas[k])
			
			if len(dests) > 0:
				x = max(dests) + 1
			else:
				print(x * 4000000 + i)
				raise 42
except:
	pass
