def largest_color_blob(arr):
	m = len(arr)
	n = len(arr[0])
	stack = []
	count = 0
	totalCount = 0
	visited = set()
	for i in range(m):
		for j in range(n):
			if (i,j) not in visited:
				count = 0
				stack.append((i,j))
				while stack:
					x, y = stack.pop()
					current_color = arr[x][y]
					visited.add((x,y))
					count +=1
					totalCount = max(count, totalCount)
					if x < m-1:
						if arr[x+1][y] == current_color and (x+1,y) not in visited:
							stack.append((x+1, y))
							visited.add((x+1,y))
 					if x > 0:
						if arr[x-1][y] == current_color and (x-1,y) not in visited:
							stack.append((x-1, y))
							visited.add((x-1,y))
					if y > 0:
						if arr[x][y-1] == current_color and (x,y-1) not in visited:
							stack.append((x, y-1))
							visited.add((x,y-1))
					if y < n-1:
						if arr[x][y+1] == current_color and (x,y+1) not in visited:
							stack.append((x, y+1))
							visited.add((x,y+1))
	return totalCount



blob = [
		['r', 'r','g','b'],
		['r', 'r','g','g'],
		['q', 'y','z','x'],
		['m', 'b','g','r'],
		['r', 'g','r','r'],

		]
print largest_color_blob(blob)