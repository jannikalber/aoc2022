import os
import sys
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")


def snafu(num):
	num = num.strip()
	number = 0
	for i in range(len(num)):
		index = -i - 1
		pow = 5 ** i
		chiffre = num[index]
		if chiffre == "-":
			chiffre = -1
		elif chiffre == "=":
			chiffre = -2
		else:
			chiffre = int(chiffre)
		number += pow * chiffre
	return number


def numberToBase(n, b):
	if n == 0:
		return [0]
	digits = []
	while n:
		digits.append(int(n % b))
		n //= b
	return digits[::-1]


list = [snafu(x) for x in file.readlines()]
sum_ = sum(list)

delta = sys.maxsize
digits_ = numberToBase(sum_, 5)
ind = 0
i = 0
while abs(ind) < len(digits_):
	ind = -i - 1
	i += 1
	chiffre = digits_[ind]
	chiffre2 = chiffre
	if chiffre >= 5:
		chiffre %= 5
		
		if abs(ind - 1) > len(digits_):
			digits_.insert(0, 0)
		
		digits_[ind - 1] += chiffre2 // 5
	
	if chiffre > 2:
		delta = 5 - chiffre
		
		if delta == 2:
			chiffre = "="
		else:
			chiffre = "-"
		
		if abs(ind - 1) > len(digits_):
			digits_.insert(0, 0)
		
		digits_[ind - 1] += 1
	
	else:
		chiffre = str(chiffre)
	
	digits_[ind] = chiffre

snafu_num = "".join(digits_)
assert sum_ == snafu(snafu_num)
print(snafu_num)
