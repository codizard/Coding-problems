def quickSort(arr):
	return quickSortHelper(arr, 0, len(arr)-1)

def quickSortHelper(arr, start, end):
	if start < end:
		pivot = arr[(start + end)//2]
		index = partition(arr, start, end, pivot)
		quickSortHelper(arr, start, index-1)
		quickSortHelper(arr, index, end)
	return arr


def partition(arr, start, end, pivot):
	while start <= end:
		while arr[start] < pivot:
			start+=1
		while arr[end] > pivot:
			end -=1
		if start <= end:
			arr[start], arr[end] = arr[end], arr[start]
			start +=1
			end -=1
	return start
print quickSort([15, 3, 9, 8, 5, 2, 7, 1, 6])