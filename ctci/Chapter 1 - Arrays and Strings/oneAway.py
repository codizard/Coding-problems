def isOneInsertAway(s1, s2):
	if abs(len(s2)- len(s1)) != 1:
		return False

	if len(s2) > s1:
		s1, s2 = s2, s1
	i, j = 0, 0
	changeDetected = False
	while i < len(s1):
		if i == len(s1) - 1 and changeDetected == True:
			return True
		if s1[i] != s2[j]:
			if changeDetected == True:
				return False
			changeDetected = True
			i = i + 1
		else:
 			i = i + 1
			j = j + 1
	return True	

def isOneRemoveAway(s1, s2):
	return True

def isOneReplaceAway(s1, s2):
	return True

def isOneAway(s1, s2):
	return isOneInsertAway(s1, s2) and isOneRemoveAway(s1, s2) and isOneReplaceAway(s1, s2)

print 1 & 1 >> 1