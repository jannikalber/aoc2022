import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

blueprints = {}
available = ["ore", "clay", "obsidian", "geode"]
rounds = 32

for i in file.readlines():
	i = i.split(": ")
	id = int(i[0].split(" ")[-1])
	
	robots = {}
	
	for j in i[1].strip().split("."):
		j = j.strip().split(" costs ")
		if len(j) < 2:
			continue
		material = j[0].split(" ")[1]
		costs = {}
		for k in j[1].split(" and "):
			k = k.split(" ")
			costs[k[1]] = int(k[0])
		for k in available:
			if k not in costs:
				costs[k] = 0
		robots[material] = costs
	
	blueprints[id] = robots


def recursive(n, array, minerals={"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}):
	global costs, geodes, rounds
	if n > rounds:
		if minerals["geode"] > geodes:
			geodes = minerals["geode"]
		return
	
	# Bound
	missing_geodes = geodes - minerals["geode"]
	if missing_geodes > 0:
		missing_rounds = rounds + 1 - n
		ccost = costs["clay"]["ore"]
		ocost = costs["obsidian"]["clay"]
		gcost = costs["geode"]["obsidian"]
		orbots = array[:-1].count("ore")
		cbots = array[:-1].count("clay")
		obots = array[:-1].count("obsidian")
		gbots = array[:-1].count("geode")
		ccrntbot = 1 if array[-1] == "clay" else 0
		ocrntbot = 1 if array[-1] == "obsidian" else 0
		gcrntbot = 1 if array[-1] == "geode" else 0
		or_ = minerals["ore"]
		c = minerals["clay"]
		o = minerals["obsidian"]
		g = minerals["geode"]
		
		for _ in range(missing_rounds):
			cnewb = 0
			onewb = 0
			gnewb = 0
			if or_ >= ccost:
				cnewb = 1
				or_ -= ccost
			if c >= ocost:
				onewb = 1
				c -= ocost
			if o >= gcost:
				gnewb = 1
				o -= gcost
			
			or_ += orbots
			c += cbots
			o += obots
			g += gbots
			
			orbots += 1
			cbots += cnewb + ccrntbot
			obots += onewb + ocrntbot
			gbots += gnewb + gcrntbot
			
			ccrntbot = 0
			ocrntbot = 0
			gcrntbot = 0
		
		if g <= geodes:
			return
	
	for j in reversed(available):
		how_much = costs[j]
		ok = False
		minutes = n
		now = -1
		minerals2 = minerals.copy()
		while not ok and minutes <= rounds:
			minutes += 1
			for i in available:
				minerals2[i] += array[:now].count(i)
			now = len(array)
			ok = True
			for co in available:
				if minerals2[co] < how_much[co]:
					ok = False
					break
		
		if ok:
			minerals3 = minerals2.copy()
			for ma in available:
				minerals3[ma] -= costs[j][ma]
			narray = array[:]
			narray.append(j)
			recursive(minutes, narray, minerals3)
		elif minutes > rounds:
			if minerals["geode"] > geodes:
				geodes = minerals["geode"]


count = 1
for key in blueprints.keys():
	if key > 3:
		continue
	costs = blueprints[key]
	geodes = 0
	recursive(1, ["ore"])
	count *= geodes
	print(f"Blueprint {key} has a maximum of {geodes} geodes")

print()
print(count)
