def mergeSort(arr):
	temp = [None] * (len(arr)-1)
	_mergeSort(arr, 0, len(arr)-1, temp)
 	print arr
def _mergeSort(arr, start, end, temp):
	if start >= end:
		return
	mid = (start + end) // 2
	_mergeSort(arr, start, mid,temp)
	_mergeSort(arr, mid+1, end,temp)
	merge(arr, start, end,temp)
def merge(arr, leftStart,rightEnd, temp):
	leftEnd = (rightEnd + leftStart)//2
	rightStart = leftEnd + 1
	size = rightEnd - leftStart + 1
	left = leftStart
	right = rightStart
	index = leftStart

	while left <= leftEnd and right <= rightEnd:
		if arr[left] <= arr[right]:
			temp[index] = arr[left]
			left +=1
		else:
			temp[index] = arr[right]
			right +=1
		index +=1
	arr[:] = temp[:]


print mergeSort([15, 3, 9, 8, 5, 2, 7, 1, 6])

