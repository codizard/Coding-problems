def maxConsecutiveZeros(array):
	count = 0
	zeros = 0
	low = 0
	high = 0
	while low < len(array) and high < len(array):
		if array[high] == 0:
			zeros +=1
		if zeros > 1:
			if array[low] == 0:
				zeros -=1
			low+=1
		count= max(count, high - low + 1)
		high +=1
	return count

print maxConsecutiveZeros([1,0,1,1,1,0,1])