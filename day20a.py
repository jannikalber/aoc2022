import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

l = [int(i) for i in file.readlines()]

order = list(range(len(l)))
mx = len(l) - 1
cr = 0

while cr <= mx:
	id = order.index(cr)
	val = l[id]
	
	nid = val + id
	if nid == id:
		cr += 1
		continue
	
	while nid > mx or nid <= 0:
		if nid > mx:
			nid = nid - mx
		elif nid <= 0:
			nid = mx + nid
	
	del order[id]
	del l[id]
	order.insert(nid, cr)
	l.insert(nid, val)
	
	cr += 1

id0 = l.index(0)
print(sum([l[(id0 + i) % len(l)] for i in [1000, 2000, 3000]]))