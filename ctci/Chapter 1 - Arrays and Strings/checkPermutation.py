def checkPermutation(s1, s2):
	if len(s1) != len (s2):
		return False

	m1 = {}
	for x in s1:
		if x in m1:
			m1[x] += 1
		else: 
			m1[x] = 1
	for i in range(0,len(s2)):
		if i == len(s2)-1:
			if s2[i] in m1 and m1[s2[i]] == 1:
				return True
			else:
				return False
		if s2[i] in m1 and m1[s2[i]] > 0:
			m1[s2[i]] -= 1
		else: 
			return False



print checkPermutation("asdaaa","daasaa") 
