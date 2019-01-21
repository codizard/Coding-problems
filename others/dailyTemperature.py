def dailyTemperatures(array):
	res = [None] * len(array)
	stack = []
	if len(array) == 0:
		return []

	i = len(array) - 1

	while i >= 0:
		if len(stack) == 0:
			stack.append((array[i], i))
		else:
			if array[i] < stack[-1][0]:
				res[i] = stack[-1][1] - i
				# stack.append((res[i], i))
			elif array[i] > stack[-1][0]:
				while len(stack) > 1 and stack[-1][0] < array[i]:
					stack.pop()
				if len(stack) > 1:
					res[i] = stack[-1][1] - i
			stack.append((array[i],i))
		i-=1

	while len(stack):
		ele, index = stack.pop()
		if res[index] is None:
			res[index] = 0
	return res

print dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])