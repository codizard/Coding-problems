def findRightPosition(array, i):
	pos = 0
	for x in array:
		if i <= x:
			return pos
		pos = pos + 1
	return pos

def insertionSort(a):
	for i in range(0, len(a)-1):
		if (a[i+1] < a[i]):
			pos = findRightPosition(a[:i+1], a[i+1])
			toAdd = a[i+1]
			del(a[i+1])
			a.insert(pos, toAdd)
	return a

