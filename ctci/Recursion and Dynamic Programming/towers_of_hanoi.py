def towers_of_hanoi(n):
	if n == 1:
		return 1
	return towers_of_hanoi(n-1) + 1 + towers_of_hanoi(n-1)

print towers_of_hanoi(4)