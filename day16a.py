import os
import sys
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

valves = {}
valves_small = {}

visited = ["AA"]

for i in file.readlines():
	i = i.strip().split("; ")
	i[0] = i[0].split(" ")
	name = i[0][1]
	rate = int(i[0][-1].split("=")[-1])
	connections = i[1].split(", ")
	connections[0] = connections[0].split(" ")[-1]
	valves[name] = {"rate": rate, "conn": connections}
	if rate > 0 or name == "AA":
		valves_small[name] = valves[name]

lst = list(valves.keys())
dis = {}
for i in range(len(lst)):
	for j in range(i + 1, len(lst)):
		from_ = lst[i]
		to_ = lst[j]
		
		abstand = {}
		vorgaenger = {}
		knoten = []
		for ii in lst:
			knoten.append(ii)
			abstand[ii] = sys.maxsize
			vorgaenger[ii] = None
		abstand[from_] = 0
		q = knoten[:]
		
		# Ab geht der Peter
		while len(q) != 0:
			mini = sys.maxsize + 1
			u = None
			for ii in q:
				if abstand[ii] < mini:
					mini = abstand[ii]
					u = ii
			q.remove(u)
			
			neighbours = {}
			for xxx in valves[u]["conn"]:
				neighbours[xxx] = 1
			
			for v in neighbours:
				if v in q:
					alternativ = abstand[u] + neighbours[v]
					if alternativ < abstand[v]:
						abstand[v] = alternativ
						vorgaenger[v] = u
		
		dis[from_ + "," + to_] = abstand[to_]
		dis[to_ + "," + from_] = abstand[to_]


def cpy(s):
	n = {}
	for i in s.keys():
		n[i] = s[i].copy()
	return n


scores = 0

container = {}
for j in valves_small.keys():
	i = valves_small[j]
	if i["rate"] in container:
		container[i["rate"]].append(j)
	else:
		container[i["rate"]] = [j]

sl = sorted(list(container.keys()), reverse=True)
lst = []
for i in sl:
	lst.extend(container[i])
lst.remove("AA")


def move(current, minutes, unvisited, score):
	global scores
	if minutes <= 0:
		if score > scores:
			scores = score
	else:
		max_s = score
		minutes2 = minutes
		for zeta in unvisited:
			minutes2 -= 1
			if minutes2 <= 0:
				break
			max_s += minutes2 * valves_small[zeta]["rate"]
		
		if max_s < scores:
			return
		
		ok = False
		for i in unvisited:
			ok = True
			u = unvisited[:]
			u.remove(i)
			minutes2 = minutes - dis[current + "," + i] - 1
			if minutes2 < 0:
				minutes2 = 0
			move(i, minutes2, u, score + minutes2 * valves_small[i]["rate"])
		if not ok and score > scores:
			scores = score


move("AA", 30, lst[:], 0)
print(scores)
