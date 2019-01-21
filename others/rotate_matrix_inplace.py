def roateMatrix(mat, N):
    # Consider all squares one by one 
    for x in range(0, int(N/2)): 
          
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, N-x-1): 
            print "x,y", x, y
              
            # store current cell in temp variable 
            temp = mat[x][y] 
  
            # move values from right to top 
            mat[x][y] = mat[N-1-x][y] 
  
            # move values from bottom to right 
            mat[N-1-y][x] = mat[N-1-x][N-1-y]

            # move values from left to bottom 
            mat[N-1-x][N-1-y] = mat[y][N-1-x]
  
            # assign temp to left 
            mat[y][N-1-x] = temp

    return mat
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print roateMatrix(matrix, len(matrix))