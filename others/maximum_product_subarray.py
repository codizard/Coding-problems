def maximum_product_subarray(arr):
	cur_max_product = arr[0]
	# cur_min_product = arr[0]
	prev_min_product = arr[0]
	prev_max_product = arr[0]
	res = arr[0]

	for i in range(1, len(arr)):
		cur_max_product = max(prev_max_product*arr[i], prev_min_product * arr[i], arr[i])
		cur_min_product = min(prev_max_product*arr[i], prev_min_product * arr[i], arr[i])
		res = max(res, cur_max_product)
		prev_min_product = cur_min_product
		prev_max_product = cur_max_product
	return res


print maximum_product_subarray([2,3,-2,4])