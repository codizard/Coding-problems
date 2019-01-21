def k_most_frequest(arr, k):
	frequency_map = {}
	res = []
	for ele in arr:
		if ele not in frequency_map:
			frequency_map[ele] = 1
		else:
			frequency_map[ele]+=1
	while k >0:
		k-=1
		i = 1
		currentFreq = frequency_map[arr[0]]
		currentString = arr[0]
		while i <len(arr):
			freq = frequency_map[arr[i]]
			if freq > currentFreq:
				currentFreq = freq
				currentString = arr[i]
			elif freq == currentFreq and currentString > arr[i]:				
				currentString = arr[i]
			i+=1
		res.append(currentString)
		print "Appended", currentString, " to res", res
		j = 0
		while j < len(arr):
			if arr[j] == currentString:
				print "Deleting", currentString, "from arr"
				del(arr[j])
			else:
				j+=1 
	return res

def k_most_frequent_using_bucket(arr, k):
	frequency_map = {}
	res = []
	bucket = [None] * (len(arr)+1)
	for ele in arr:
		if ele not in frequency_map:
			frequency_map[ele] = 1
		else:
			frequency_map[ele]+=1

	for key in frequency_map.keys():
		if bucket[frequency_map[key]] is None:
			bucket[frequency_map[key]] = [key]
		else:
			bucket[frequency_map[key]].append(key)
	print bucket
	while k > 0:
		for i in range(len(bucket)-1, -1, -1):
			if bucket[i] is not None:
				if len(bucket[i]) < k:
					res.append(bucket[i])
					k-=len(bucket[i])
					print "Added", bucket[i], "to res and the new K value is", k
 				else:
					for x in bucket[i]:
						res.append(x)
						k-=1
						if k == 0:
							return res
	return res

# print "a" < "A"
# print k_most_frequest(["i", "love", "leetcode", "i", "love", "coding", "love", "leetcode", "xyz", "leetcode"], 4)
print k_most_frequent_using_bucket([1,1,2,3,4,2,3,3], 2)