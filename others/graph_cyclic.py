def isGraphCyclicUtil(v, visited, recStack, nodeMap):

	visited[v] = True
	recStack[v] = True

	if v in nodeMap:
		for neighbour in nodeMap[v]:
			if visited[neighbour] == False:
				if isGraphCyclicUtil(neighbour, visited, recStack, nodeMap) == True:
					return True
			else:
				if recStack[neighbour] == True:
					return True
	recStack[v] = False
	return False



def isGraphCyclic(numNodes, graph):
	nodeMap = {}
	for x in graph:
		if x[0] not in nodeMap:
			nodeMap[x[0]] = [x[1]]
		else:
			nodeMap[x[0]].append(x[1])

	visited = [False] * numNodes
	recStack = [False] * numNodes

	for i in range(numNodes):
		if isGraphCyclicUtil(i, visited, recStack, nodeMap) == True:
			return True
	return False
	# pass

print isGraphCyclic(4, [[0, 1], [1, 2], [2,3]])