def fruit_basket(arr):
	visited = set()
	visited.add(arr[0])
	queue = [(arr[0], 1)]
	totalCount = 1
	for i in range(1, len(arr)):
		if arr[i] in visited:
			if len(visited) < 2:
				visited.add(arr[i])
				totalCount += 1
				queue.append(arr[i], 1)
			else:
				ele, count = queue.pop(0)
				totalCount -= count
				queue(arr[i], 1)
				


	pass

arr = [1,2,1,3,4,3,4,5]
print fruit_basket(arr)
