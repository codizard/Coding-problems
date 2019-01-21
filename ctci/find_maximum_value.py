def minimumValue(dp, ele):
	minVal = float('inf')
	for num in dp:
		add = num + ele
		sub = num - ele
		mul = num * ele
		if ele != 0:
			div = num / ele
		else:
			div = float('inf')
		minVal = min(minVal, add, sub, mul, div)
	return minVal
def maximumValue(dp, ele):
	maxVal = float('-inf')
	for num in dp:
		add = num + ele
		sub = num - ele
		mul = num * ele
		if ele != 0:
			div = num / ele
		else:
			div = float('-inf')
		maxVal = max(maxVal, add, sub, mul, div)
	return maxVal

def findMaxValue(arr):
	dp = [None] * len(arr)
	if len(arr) == 0:
		return 0
	dp[0] = (arr[0], arr[0])
	for i in range(1, len(arr)):
		dp[i] = (minimumValue(dp[i-1], arr[i]), maximumValue(dp[i-1], arr[i]))
	return max(dp[len(dp)-1])


print findMaxValue([-1, -2, -1])


