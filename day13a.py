import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")


def compare(left, right):
	if type(left) == int and type(right) == int:
		if left < right:
			return True
		elif left == right:
			return None
		else:
			return False
	elif type(left) == list and type(right) == list:
		for i in range(min([len(left), len(right)])):
			l = left[i]
			r = right[i]
			
			val = compare(l, r)
			if val is not None:
				return val
		if len(left) < len(right):
			return True
		elif len(left) > len(right):
			return False
		else:
			return None
	elif type(left) == list and type(right) == int:
		return compare(left, [right])
	elif type(left) == int and type(right) == list:
		return compare([left], right)
	else:
		raise


con = file.read().strip().split("\n\n")
correct = []
for ii in range(len(con)):
	i = con[ii]
	i = i.split("\n")
	left = None
	right = None
	
	exec("left=" + i[0])
	exec("right=" + i[1])
	
	val = compare(left, right)
	if val is None or val:
		correct.append(ii+1)
		
print(sum(correct))
