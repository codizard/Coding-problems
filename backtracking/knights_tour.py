def knights_tour(N):
	sol = [[-1 for i in range(N)] for j in range(N)]

	moves = set([(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)])

	sol[0][0] = 0

	currentMove = 1

	if knights_tour_recur(0, 0, currentMove, sol, moves, N):
		print sol
	else:
		print "No solution"

def knights_tour_recur(curX, curY, currentMove, sol, moves, N):
	if currentMove == N * N:
		return True

	for move in moves:
		nextX = curX + move[0]
		nextY = curY + move[1]

		if isValidMove(nextX, nextY, sol, N):
			sol[nextX][nextY] = currentMove

			if knights_tour_recur(nextX, nextY, currentMove+1, sol, moves, N):
				return True
			else:
				sol[nextX][nextY] = -1

	return False

def isValidMove(X, Y, sol, N):
	if X >= 0 and X < N and Y >= 0 and Y < N and sol[X][Y] == -1:
		return True
	return False

knights_tour(8)
