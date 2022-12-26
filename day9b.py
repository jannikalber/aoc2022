import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

position = set()
x = 10 * [0]
y = 10 * [0]


def move(k):
	if (x[k] - x[k - 1]) ** 2 + (y[k] - y[k - 1]) ** 2 == 4:
		a = x[k]
		b = y[k]
		available = [[a - 1, b], [a + 1, b], [a, b + 1], [a, b - 1]]
		dis = len(available) * [999999]
		for l in range(len(available)):
			dis[l] = (x[k - 1] - available[l][0]) ** 2 + (y[k - 1] - available[l][1]) ** 2
		
		winner = available[dis.index(min(dis))]
		
		x[k] = winner[0]
		y[k] = winner[1]
	elif (x[k] - x[k - 1]) ** 2 + (y[k] - y[k - 1]) ** 2 > 4:
		a = x[k]
		b = y[k]
		available = [[a - 1, b - 1], [a + 1, b - 1], [a + 1, b + 1], [a - 1, b + 1]]
		dis = len(available) * [999999]
		for l in range(len(available)):
			dis[l] = (x[k - 1] - available[l][0]) ** 2 + (y[k - 1] - available[l][1]) ** 2
		
		winner = available[dis.index(min(dis))]
		
		x[k] = winner[0]
		y[k] = winner[1]
	
	elif (x[k] - x[k - 1]) ** 2 + (y[k] - y[k - 1]) ** 2 <= 2:
		pass


for i in file.readlines():
	i = i.split(" ")
	pos = {"R": [1, 0], "L": [-1, 0], "U": [0, 1], "D": [0, -1]}[i[0]]
	cnt = int(i[1])
	for j in range(cnt):
		x[0] += pos[0]
		y[0] += pos[1]
		
		for k in range(1, 10):
			move(k)
		position.add(str([x[9], y[9]]))

print(len(position))
