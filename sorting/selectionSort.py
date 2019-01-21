def findIndexOfMinElement(a):
	if len(a) == 0:
		return -1
	else:
		minIndex, minElement = 0, a[0]
		for i in range(len(a)):
			if a[i] < minElement:
				minIndex = i
				minElement = a[i]
	return minIndex

def selectionSort(a):
	for i in range(len(a)):
		minIndex = findIndexOfMinElement(a[i:])
		toDel = a[minIndex+i]
		del a[minIndex+i]
		a.insert(i, toDel)
	return a
