def isPalindromePermutation(string):
	myMap = {}
	for x in string:
		if x not in myMap:
			myMap[x] = 1
		else:
			myMap[x] = myMap[x] + 1
	isOdd = False
	print myMap
	for m in myMap:
		if myMap[m] %2 != 0:
			if isOdd == True:
				return False
			isOdd = True
	return True
		

print isPalindromePermutation('taaccocat')
