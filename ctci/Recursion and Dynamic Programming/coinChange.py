def coinChange(arr, target, index):
	if target == 0:
		return 1
	if index >= len(arr):
		return 0
	ways = 0
	amountMadeUntilNow = 0
	while amountMadeUntilNow <= target:
		remaining = target-amountMadeUntilNow
		ways +=coinChange(arr, remaining, index +1)
		amountMadeUntilNow +=arr[index]
	return ways

print coinChange([1,2,3], 4, 0)



	# if target == 0:
	# 	return 1
	# elif index >= len(arr):
	# 	return 0
	# ways = 0
	# moneyMadeTillNow = 0
	# while moneyMadeTillNow <= target:
	# 	remaining = target - moneyMadeTillNow
	# 	ways += coinChange(arr, remaining , index + 1)
	# 	moneyMadeTillNow += arr[index]

	# return ways