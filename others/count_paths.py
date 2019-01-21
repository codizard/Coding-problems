def countPathIter(grid, m, n):
	res = [[None for i in range(0,n)] for j in range(0,m)]
	for i in range(0,m):
		for j in range(0,n):
			if i ==0 or j == 0:
				if grid[i][j] == 0:
					res[i][j] = 1
				elif grid[i][j] == 1:
					res[i][j] = 0
			else:
				if grid[i][j] == 0:
					res[i][j] = res[i-1][j] + res[i][j-1]
				else:
					res[i][j] = 0

	# print res
	return res[m-1][n-1]



arr = [
  [0,0,0],
  [0,1,0],
  [0,0,0],
  [0,0,0]
]
print countPathIter(arr, 4, 3)