def find_last_index(arr, start, end, target):
	while start <= end:
		mid = (start + end) // 2
		if arr[mid] == target:
			if mid == len(arr)-1:
				return mid
			elif arr[mid+1] > arr[mid]:
				start = mid + 1
		elif arr[mid] > target:
			end = mid-1
		else:
			start = mid + 1
	
	return (start + end ) // 2




def insert_into_sorted_array(arr, k):
	print find_last_index(arr, 0, len(arr), k)


arr = [1, 2, 10, 90, 100, 231, 441]
k = 101

insert_into_sorted_array(arr, k)
