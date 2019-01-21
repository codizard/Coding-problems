from numpy import median
def array_median(arr1, arr2):
	i, j, k = 0, 0, 0
	m = len(arr1)
	n = len(arr2)
	median_index = round((m+n)/2)

	if m == 0:
		return median(arr2)
	if n == 0:
		return median(arr1)

	while i < m and j < n:
		# print i, j
		if k == median_index:
			# print "k, median_index, i, j", k, median_index, i, j
			if median_index % 2 == 0:
				if i < m -1 and j < n-1:
					return (min(arr1[i], arr2[j]) + min(arr1[i+1], arr2[j+1]))//float(2)
				elif i < m-1:
					return min(arr1[i], arr2[j]) + arr1[i+1]//float(2)
				elif j < n-1:
					return min(arr1[i], arr2[j]) + arr2[j+1]//float(2)
			else:
				return min(arr1[i], arr2[j])
		if arr1[i] < arr2[j]:
			i+=1
			k+=1
		elif arr1[i] > arr2[j]:
			j+=1
			k+=1
	while i < m:
		if k == median_index:
			print "here", median_index
			if median_index % 2 == 0:
				return (arr1[i] + arr1[i+1]) // float(2)
			else:
				return arr1[i]

		i+=1
		k+=1
	while j < n:
		if k == median_index:
			if median_index % 2 == 0:
				return (arr2[j] + arr1[j+1]) // float(2)
			else:
				return arr2[j]

		j+=1
		k+=1 
	

print array_median([1,2,3,6,10], [0])