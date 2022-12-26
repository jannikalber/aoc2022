import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

blizzards_r = []
blizzards_l = []
blizzards_d = []
blizzards_u = []

read = file.readlines()

max_y = len(read)
modulo_y = max_y - 2
max_x = len(read[0].strip())
modulo_x = max_x - 2

for ii in range(len(read)):
	thisline_blizzards_r = []
	thisline_blizzards_l = []
	for jj in range(len(read[0].strip())):
		if jj + 1 > len(blizzards_d):
			blizzards_d.append([])
			blizzards_u.append([])
		crnt = read[ii][jj]
		
		if crnt == ">":
			thisline_blizzards_r.append(jj)
		elif crnt == "<":
			thisline_blizzards_l.append(jj)
		elif crnt == "^":
			blizzards_u[jj].append(ii)
		elif crnt == "v":
			blizzards_d[jj].append(ii)
	
	blizzards_r.append(thisline_blizzards_r)
	blizzards_l.append(thisline_blizzards_l)


def simulate(br, bl, bu, bd):
	for ii in range(len(br)):
		for _ in range(len(br[ii])):
			val = br[ii].pop(0)
			val %= modulo_x
			br[ii].append(val + 1)
	
	for ii in range(len(bl)):
		for _ in range(len(bl[ii])):
			val = bl[ii].pop(0) - 2
			val %= modulo_x
			bl[ii].append(val + 1)
	
	for ii in range(len(bu)):
		for _ in range(len(bu[ii])):
			val = bu[ii].pop(0) - 2
			val %= modulo_y
			bu[ii].append(val + 1)
	
	for ii in range(len(bd)):
		for _ in range(len(bd[ii])):
			val = bd[ii].pop(0)
			val %= modulo_y
			bd[ii].append(val + 1)


blr = [blizzards_r]
bll = [blizzards_l]
blu = [blizzards_u]
bld = [blizzards_d]


def require(to):
	global blr, bll, bld, blu
	crnt_level = len(blr) - 1
	while crnt_level < to:
		blrn = [x[:] for x in blr[crnt_level]]
		blln = [x[:] for x in bll[crnt_level]]
		blun = [x[:] for x in blu[crnt_level]]
		bldn = [x[:] for x in bld[crnt_level]]
		simulate(blrn, blln, blun, bldn)
		blr.append(blrn)
		bll.append(blln)
		blu.append(blun)
		bld.append(bldn)
		crnt_level = len(blr) - 1


def solve(start, end, minute=0):
	max = - 1
	minq = [minute]
	posq = [start]
	done = set()
	
	while len(minq) > 0:
		min = minq.pop(0)
		pos = posq.pop(0)
		
		if str([min, pos]) in done:
			continue
		else:
			done.add(str([min, pos]))
		
		if pos == end:
			max = min
			break
		else:
			new_min = min + 1
			require(new_min)
			for todo in [[0, 1], [0, -1], [1, 0], [-1, 0], [0, 0]]:
				pos2 = pos[:]
				for x in range(2):
					pos2[x] += todo[x]
				
				if 0 <= pos2[0] <= max_x - 1 and 0 <= pos2[1] <= max_y - 1 and read[pos2[1]][
					pos2[0]] != "#" and pos2[0] not in blr[new_min][pos2[1]] and pos2[0] not in bll[new_min][
					pos2[1]] and \
						pos2[1] not in blu[new_min][pos2[0]] and pos2[1] not in bld[new_min][pos2[0]]:
					minq.append(new_min)
					posq.append(pos2)
					
	return max


start = [1, 0]
target = [len(read[0].strip()) - 2, len(read) - 1]

print(solve(start, target, solve(target, start, solve(start, target))))
