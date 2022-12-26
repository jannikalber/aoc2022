import os
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

start = None
target = None
view = [list(x.strip()) for x in file.readlines()]

for i in range(len(view)):
	for j in range(len(view[i])):
		if view[i][j] == "S":
			start = [i, j]
			view[i][j] = "a"
		elif view[i][j] == "E":
			target = [i, j]
			view[i][j] = "z"


def is_visible(from_, toi):
	colf = from_ // len(view)
	rowf = from_ % len(view)
	
	colt = toi // len(view)
	rowt = toi % len(view)
	
	if (rowt - rowf) ** 2 + (colt - colf) ** 2 != 1:
		return False
	
	fromo = ord(view[rowf][colf])
	too = ord(view[rowt][colt])
	
	return too <= fromo + 1


def bfs(start):
	# A Queue to manage the nodes that have yet to be visited, intialized with the start node
	queue = [start]
	len_graph = len(view) * len(view[0])
	# A boolean array indicating whether we have already visited a node
	visited = [False] * (len_graph ** 2)
	# (The start node is already visited)
	visited[start] = True
	# Keeping the distances (might not be necessary depending on your use case)
	distances = [float("inf")] * (
			len_graph ** 2)  # Technically no need to set initial values since every node is visted exactly once
	# (the distance to the start node is 0)
	distances[start] = 0
	# While there are nodes left to visit...
	while len(queue) > 0:
		node = queue.pop(0)
		# ...for all neighboring nodes that haven't been visited yet....
		for i in range(len_graph):
			if is_visible(node, i) and not visited[i]:
				# Do whatever you want to do with the node here.
				# Visit it, set the distance and add it to the queue
				visited[i] = True
				distances[i] = distances[node] + 1
				queue.append(i)
	
	return distances


print(bfs(len(view) * start[1] + start[0])[len(view) * target[1] + target[0]])
