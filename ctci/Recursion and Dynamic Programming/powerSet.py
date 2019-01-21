def powerSet(nums, chosen, index, res):
	if index >= len(nums):
		res+= chosen + [" "]
	else:
		chosen.append(nums[index])
		temp = nums[index]
		nums[index] = None
		powerSet(nums, chosen, index+1, res)
		chosen.pop(-1)
		nums[index] = temp
		powerSet(nums, chosen, index + 1, res)

def convert_to_array(res):
	n = []
	temp = []
	for x in res:
		if x == " ":
			n.append("".join(temp))
			temp = []
		else:
			temp.append(x)
	return n

def find_largest_common(p1, p2):
	for x in p1:
		if x in p2:
			ans = x
	return ans

	# i = len(p1)-1
	# j = len(p2) -1

	# while i > 0 and j > 0:
	# 	if p1[i] == p2[j]:
	# 		return p1[i]
	# 	elif len(p1[i]) > len(p2[j]):
	# 		i-=1
	# 	elif len(p1[i]) < len(p2[j]):
	# 		j-=1
	# 	elif len(p1[i]) == len(p2[j]):
	# 		i-=1
	# 		j-=1
	# return " "


def lcs(s1, s2):
	res = []
	powerSet(list(s1), [], 0, res)
	p1 = convert_to_array(res)
	res = []
	powerSet(list(s2), [], 0, res)
	p2 = convert_to_array(res)
	p1.sort(key = lambda s: len(s))
	p2.sort(key = lambda s: len(s))
	# print p1
	# print p2
	return find_largest_common(p1, p2)

print lcs("ABCDGH", "AEDFHR")
