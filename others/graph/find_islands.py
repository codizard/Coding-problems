def find_number_islands(arr):
    m = len(arr)
    n = len(arr[0])
    stack = []
    numberOfIslands = 0
    i, j, =0, 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                numberOfIslands +=1
                # print "Arr", arr

                # arr[i][j] = 0
                stack = [(i,j)]
                while stack:
                    x, y = stack.pop()
                    arr[x][y] = 0
                    if x < m-1:
                        if arr[x+1][y] == 1:
                            stack.append((x+1, y))
                    if y < n-1:
                        if arr[x][y+1] == 1:
                            stack.append((x, y+1))
                    if x > 0:
                        if arr[x-1][y] == 1:
                            stack.append((x-1, y))
                    if y > 0:
                        if arr[x][y-1] == 1:
                            stack.append((x, y-1))
    # print arr
    return numberOfIslands


arr = [
        [1,1,1,0,0],
        [0,0,0,0,1],
        [1,1,1,0,1]
    ]
print find_number_islands(arr)






'''
    for i in range(0, m):
        for j in range(0, n):
            if arr[i][j] == 1:
                arr[i][j] = 0
                if i < m-1:
                    stack.append((i+1, j)) #j == n, i, == m
                if j < n-1:
                    stack.append((j+1, i))
                while len(stack):
                    x, y = stack.pop()
                    arr[x][y] = 0
                    if x < m-1:
                        if arr[x+1][y] == 1:
                            stack.append((x+1,y))
                            hasOne = True
                    if y < n-1:
                        if arr[x][y+1] == 1:
                            stack.append((x,y+1))
                            hasOne = True
                    if not hasOne:
                        numberOfIslands += 1
                    else:
                        hasOne = False
    return numberOfIslands

'''