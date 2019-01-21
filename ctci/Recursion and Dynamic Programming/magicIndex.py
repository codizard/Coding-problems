#return i == a[i] for a given sorted array

def binSearch(arr, start, end):
	if start <= end:
		mid = (start + end) // 2
		if arr[mid] == mid:
			return mid
		elif arr[mid] > mid:
			return binSearch(arr, start, mid-1)
		else:
			return binSearch(arr, mid+1, end)
	return -1

def magicIndex(arr):
	return binSearch(arr, 0, len(arr)-1)


arr = [ -10, -1, 0, 2, 3, 6, 10, 12, 12 ,12, 100]
print magicIndex(arr)
