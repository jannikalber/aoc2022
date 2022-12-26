import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

l = [int(i) * 811589153 for i in file.readlines()]
ll = []
for i in l:
	n = abs(i) % (len(l) - 1)
	if i < 0:
		n = -n
	ll.append(n)

order = list(range(len(l)))
for _ in range(10):
	mx = len(l) - 1
	cr = 0
	
	while cr <= mx:
		id = order.index(cr)
		val = ll[id]
		oval = l[id]
		
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
		del ll[id]
		order.insert(nid, cr)
		l.insert(nid, oval)
		ll.insert(nid, val)
		
		cr += 1

id0 = l.index(0)
print(sum([l[(id0 + i) % len(l)] for i in [1000, 2000, 3000]]))
