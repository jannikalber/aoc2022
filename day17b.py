import os
import sys
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

pattern = file.read().strip()
shapes = [["####"], [".#.", "###", ".#."], ["..#", "..#", "###"], ["#", "#", "#", "#"], ["##", "##"]]

chamber = []
diff = 0
topest = 0
shapei = 0
patterni = 0

lasts = -1
lastp = -1
lasth = 0
log = []


def reinit():
	global topest, shapei, patterni, chamber, diff, lasth, lasts, lastp, log
	topest = 0
	shapei = 0
	patterni = 0
	
	chamber = []
	for i in range(150):
		chamber.append(7 * ["."])
	
	diff = 0
	lasth = 0
	lasts = -1
	lastp = -1
	log = []


reinit()


def simulate(cnt, p=sys.maxsize):
	global topest, shapei, patterni, chamber, diff, lasth, lastp, lasts, log
	for round in range(cnt):
		shape = shapes[shapei]
		y = topest + 5
		x = 2
		
		if y + len(shape) - 1 > len(chamber) + diff:
			for _ in range(y + len(shape) - 1 - len(chamber) - diff):
				chamber.insert(0, 7 * ["."])
		
		ok = True
		while ok:
			for mover in [[-1, 0], "i"]:
				if not ok:
					continue
				if mover == "i":
					mover = pattern[patterni]
					if mover == ">":
						mover = [0, 1]
					else:
						mover = [0, -1]
					patterni = (patterni + 1) % len(pattern)
				
				try:
					for add_y in range(len(shape) - 1, -1, -1):
						for add_x in range(len(shape[0])):
							if shape[len(shape) - 1 - add_y][add_x] == "#":
								target_x = x + add_x + mover[1]
								target_y = y + add_y + mover[0]
								
								if target_y < 1 or (
										0 <= target_x < 7 and chamber[-(target_y - diff)][target_x] == "#" and mover[
									1] == 0):
									ok = False
									raise TimeoutError()
								
								if not 0 <= target_x < 7 or chamber[-(target_y - diff)][target_x] == "#":
									raise TimeoutError()
					
					x += mover[1]
					y += mover[0]
				except TimeoutError:
					pass
		
		# Position it
		for add_y in range(len(shape) - 1, -1, -1):
			for add_x in range(len(shape[0])):
				if shape[len(shape) - 1 - add_y][add_x] == "#":
					chamber[-(y + add_y - diff)][x + add_x] = "#"
		topestl = y + len(shape) - 1
		if topestl > topest:
			topest = topestl
		shapei = (shapei + 1) % len(shapes)
		
		if round % p == 0:
			log.append(topest - lasth)
			
			lasth = topest
			lastp = patterni
			lasts = shapei


simulate(10000, 1)
period = -1
possible = -1
crnt = 15
while period == -1:
	lst = log[-crnt:]
	indexes = [i for i in range(len(log)) if log[i:i + len(lst)] == lst]
	
	crnt += 50
	if crnt > len(log):
		print("Period search failed. Please restart...")
	elif len(indexes) > 2:
		dis = indexes[1] - indexes[0]
		
		okay = True
		last = indexes[0]
		for i in indexes[1:]:
			if last + dis != i:
				okay = False
				break
			last = i
		
		if okay:
			reinit()
			simulate(10000, dis)
			period = dis
			possible = log[-1]

to_sim = 0
for i in log:
	if i != possible:
		to_sim += 1
	else:
		break

print(f"p = {period}")
print(f"After {to_sim * period}={to_sim}p rounds first repeating")

maximum = 1000000000000
reinit()
simulate(to_sim * period)

heightb = topest
patternib = patterni
shapeib = shapei
simulate(period)

rounds_done = (to_sim + 1) * period
period_height = topest - heightb

sim = maximum - rounds_done
counter = sim // period
print(f"Skipping {counter * period} rounds")

then_remaining = sim % period
topest += counter * period_height
diff += counter * period_height
shapei = shapeib
patterni = patternib
simulate(then_remaining)

print()
print(topest)
