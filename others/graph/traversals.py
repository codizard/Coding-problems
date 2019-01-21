def bfs(numNodes, graph):
	g_map = {}
	for x in graph:
		if x[0] not in g_map:
			g_map[x[0]] = [x[1]]
		else:
			g_map[x[0]].append(x[1])

	queue = []
	res = []
	visited = [False] * numNodes
	for i in range(numNodes):
		if not visited[i]:
			queue = [i]
			while len(queue) > 0:
				cur = queue.pop(0)
				res.append(cur)
				if cur in g_map:
					for neighbour in g_map[cur]:
						if not visited[neighbour]:
							queue.append(neighbour)
							visited[neighbour] = True

	return res


def dfs(numNodes, graph):
	def dfsUtil(v, visited, g_map, stack):
		visited[v] = True
		stack+=[v]
		if v in g_map:
			for neighbour in g_map[v]:
				if not visited[neighbour]:
					dfsUtil(neighbour, visited, g_map, stack)

	g_map = {}
	stack = []
	for x in graph:
		if x[0] not in g_map:
			g_map[x[0]] = [x[1]]
		else:
			g_map[x[0]].append(x[1])
	visited = [False] * numNodes
	for i in range(numNodes):
		if not visited[i]:
			dfsUtil(i, visited, g_map, stack)

	return stack

graph = [[0,1], [1, 2], [5, 3],[3,4], [0,5]]
# print bfs(6, graph)
print dfs(6, graph)