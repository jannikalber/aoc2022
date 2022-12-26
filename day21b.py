import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

inst = {}
for i in file.readlines():
	i = i.strip().split(": ")
	inst[i[0]] = i[1].split(" ")

vals = {}
variable = {}


def init(m):
	global variable
	ins = inst[m]
	if len(ins) == 1:
		if m == "humn":
			variable[m] = True
			return True
		else:
			variable[m] = False
			return False
	else:
		r1 = init(ins[0])
		r2 = init(ins[2])
		r = r1 or r2
		variable[m] = r
		return r


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
		exec("rtrn =" + str(l) + ins[1] + str(r), variables)
		rtrn = variables["rtrn"]
		vals[m] = rtrn
		return rtrn


def res2(m, should_be):
	global vals, variable
	ins = inst[m]
	if len(ins) == 1:
		print(int(should_be))
	else:
		nop = ins[1]
		if nop == "+":
			nop = "-"
		elif nop == "-":
			nop = "+"
		elif nop == "*":
			nop = "/"
		elif nop == "/":
			nop = "*"
		
		if variable[ins[0]]:
			exc = "rtrn = " + str(should_be) + nop + str(res(ins[2]))
			variables = {}
			exec(exc, variables)
			res2(ins[0], variables["rtrn"])
		
		else:
			if ins[1] in "-/":
				exc = "rtrn = " + str(res(ins[0])) + ins[1] + str(should_be)
			else:
				exc = "rtrn = " + str(should_be) + nop + str(res(ins[0]))
			
			variables = {}
			exec(exc, variables)
			res2(ins[2], variables["rtrn"])


init("root")
root = inst["root"]
if variable[root[0]]:
	res2(root[0], res(root[2]))
else:
	res2(root[2], res(root[0]))
