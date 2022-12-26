import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

monkeys = []
input = file.read().split("\n\n")

for i in input:
	i = i.split("\n")
	monkey = {}
	
	monkey["items"] = [int(x) for x in i[1].split(": ")[1].split(", ")]
	monkey["operation"] = i[2].split(": ")[1]
	monkey["test"] = int(i[3].split(" divisible by ")[1])
	monkey["true"] = int(i[4].split(" to monkey ")[1])
	monkey["false"] = int(i[5].split(" to monkey ")[1])
	monkey["count"] = 0
	
	monkeys.append(monkey)


def kgV(zahlen):
	mal = 1
	while True:
		vielfaches = zahlen[0] * mal
		try:
			for zahl in zahlen:
				rest = (vielfaches % zahl)
				if not rest:
					pass
				else:
					raise
			break
		except:
			pass
		mal += 1
	return vielfaches


kgv = kgV([x["test"] for x in monkeys])

for r in range(10000):
	for m in monkeys:
		while len(m["items"]) > 0:
			item = m["items"].pop(0)
			m["count"] += 1
			old = item % kgv
			new = 0
			exec(m["operation"])
			item = new % kgv
			
			if item % m["test"] == 0:
				target = monkeys[m["true"]]
			else:
				target = monkeys[m["false"]]
			
			target["items"].append(item)

list = [m["count"] for m in monkeys]
m = max(list)
list.remove(m)
print(max(list) * m)
