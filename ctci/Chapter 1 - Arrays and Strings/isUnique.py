def isUniqueWithHashmap(s):
	myMap = {}
	for x in s:
		if x in myMap:
			return False
		myMap[x] = s
	return True

def isUniqueWithArray(s):
	myArray = [None] * 128
	for x in s:
		if myArray[ord(x)] == True:
			return False
		myArray[ord(x)] = True
	return True

def isUniqueWithoutExtraMemory(s):
	for i in range(len(s)):
		for j in range(i+1, len(s)):
			if s[i] == s[j]:
				return False
	return True

print isUniqueWithoutExtraMemory("aqwepoj211")
