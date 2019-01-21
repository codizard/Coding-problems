def countSteps(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 3


	res = [0] * (n+1)
	res[1] = 1
	res[2] = 2
	res[3] = 3
	for i in range(4, n+1):
		res[i] = res[i-1] + res[i-2] + res[i-3]

	return res[-1]

print countSteps(100)