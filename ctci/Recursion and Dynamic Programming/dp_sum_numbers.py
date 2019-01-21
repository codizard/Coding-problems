# Given 3 numbers {1, 3, 5}, we need to tell
# the total number of ways we can form a number 'N' 
# using the sum of the given three numbers.


'''
sum > N:
	return
sum == N:
	print 
	return
sum < N:
	choose[0]
	f()
	unchoose
	choose[1]
	f()
	choose[2]


'''
def _sum(s, N, currentSum, memo):
	# print "_sum (", s, " ", N, " ", currentSum, ")"
	# global ways
	if currentSum > N:
		return 0 
	if currentSum == N:
		return 1
	if currentSum not in memo:
		ways = 0
		for x in s:
			currentSum+= x
			ways += _sum(s, N, currentSum, memo)
			if currentSum not in memo:
				memo[currentSum] = ways
			currentSum-=x
		return ways
	else:
		return memo[currentSum]
print _sum([1,3,5], 6, 0, {})
# print ways