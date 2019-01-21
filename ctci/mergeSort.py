def mergeSort(arr):
	_mergeSort(arr, 0, len(arr)-1)
	print arr
def _mergeSort(arr, start, end):
	if start < end:
		mid = (start + end) //2 
		_mergeSort(arr, start, mid)
		_mergeSort(arr, mid+1, end)
		merge(arr, start, mid, end)

def merge(arr, start, mid, end):
	a_size = mid - start + 1
	b_size = end - mid
	a = [None] * a_size
	b = [None] * b_size

	a[:] = arr[start:start + a_size]
	b[:] = arr[mid+1: mid + b_size+1]

	i, j = 0, 0
	k = start


	while i < a_size and j < b_size:
		if a[i] <= b[j]:
			arr[k] = a[i]
			i+=1
		else:
			arr[k] = b[j]
			j+=1
		k+=1
	while i < a_size:
		arr[k] = a[i]
		k+=1
		i+=1
	while j < b_size:
		arr[k] = b[j]
		j+=1
		k+=1




mergeSort([20,10,2,3,100,9])
