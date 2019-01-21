def longest_increasing_subsequence(arr):
	L = [0] * len(arr)
	
	L[0] = 1
	for i in range(1, len(arr)):
		j = i-1
		while j >= 0:
			if arr[i] > arr[j]:
				L[i] = max(L[i], 1 + L[j])
			j-=1
	return L[-1]

print longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60])