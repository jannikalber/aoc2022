import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

inst = {}
for i in file.readlines():
	i = i.strip().split(": ")
	inst[i[0]] = i[1].split(" ")

vals = {}


def res(m):
	global vals
	ins = inst[m]
	if len(ins) == 1:
		vals[m] = int(ins[0])
		return int(ins[0])
	else:
		if ins[0] not in vals:
			l = res(ins[0])
		else:
			l = vals(ins[0])
		if ins[2] not in vals:
			r = res(ins[2])
		else:
			r = vals(ins[2])
		variables = {}
		exec("rtrn = " + str(l) + ins[1] + str(r), variables)
		rtrn = variables["rtrn"]
		vals[m] = rtrn
		return rtrn


print(int(res("root")))
