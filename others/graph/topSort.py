def topSortUtil(v, stack, visited, courseMap):
    visited.add(v)
    if v in courseMap:
        for x in courseMap[v]:
            if x not in visited:
                topSortUtil(x, stack, visited, courseMap)
    
    stack.insert(0, v)

def topSort(numNodes, graph):
    courseMap = {}
    for i in range(len(graph)):
        if graph[i][0] not in courseMap:
            courseMap[graph[i][0]] = [graph[i][1]]
        else:
            courseMap[graph[i][0]].append(graph[i][1])
    # print courseMap
    visited = set()
    stack = []
    for i in range(numNodes):
        if i not in visited:
            topSortUtil(i, stack, visited, courseMap)
    return stack
    # return len(stack) == numNodes
l = {0:"a", 1 : "b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i"}
for res in topSort(2, [[0, 1], [1, 0]]):
    print l[res].upper(),