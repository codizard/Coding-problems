def nextGreaterElement(array):
	m = {}
	i = 0
	n = len(array)
	s = []
	while i < n:
		if len(s) == 0:
			s.append(array[i])
			i+=1
		else:
			while len(s) > 0 and s[-1] < array[i]:
				cur = s.pop()
				m[cur] = array[i]
			s.append(array[i])
			i+=1
	while len(s) != 0:
		cur = s.pop()
		m[cur] = -1
	return m

print nextGreaterElement([2, 0, 1, -1, 3])