def sqrt(x):
	def binSearch(start, end, target):
		mid = None
		while start < end:
			prevMid = mid
			mid = (start + end) / float(2)
			if mid == prevMid:
				return mid
			if mid * mid == target:
				return mid
			elif mid * mid < target: 
				start = mid
			else:
				end = mid
		return -1
	if x < 0:
		return "error"
	else:
		return binSearch(0, x, x)


print sqrt(3)