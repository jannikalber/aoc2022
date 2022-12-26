import os
import functools
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
my_list = [[[2]], [[6]]]
for ii in range(len(con)):
	i = con[ii]
	i = i.split("\n")
	left = None
	right = None
	
	exec("left=" + i[0])
	exec("right=" + i[1])
	
	my_list.append(left)
	my_list.append(right)


def compare2(i1, i2):
	if compare(i1, i2):
		return -1
	elif compare(i2, i1):
		return 1
	else:
		return 0


my_list.sort(key=functools.cmp_to_key(compare2))
print((my_list.index([[2]]) + 1) * (my_list.index([[6]]) + 1))
