def quickSort(arr):
	return _quickSort(arr, 0, len(arr)-1)

def _quickSort(arr, start, end):
	if start >=  end:
		return
	pivot = arr[(start+end)/2]
	index = partition(arr, start, end, pivot)
	_quickSort(arr, start, index-1)
	_quickSort(arr, index, end)
	return arr

def partition(arr, start, end, pivot):
	while start <= end:
		if arr[start] < pivot:
			start +=1
		elif arr[end] > pivot:
			end-=1
		elif arr[start] >= pivot and arr[end] <= pivot:
			arr[start], arr[end] = arr[end], arr[start]
			start +=1
			end-=1
	return start

print quickSort([1,3,3,1,3,2,4,5,1,3,5,1,111,2,0]) 