count = 0
def powerSet(string, chosen, index, res):
	global count
	count +=1
	print "Power Set", count
	if index > len(string)-1:
		res += chosen + [" "]
		return
	else:
	
		temp = string[index]
		chosen.append(string[index])
		string[index] = None
		powerSet(string, chosen, index+1, res)
		chosen.pop(len(chosen)-1)
		string[index] = temp
		powerSet(string, chosen, index+1, res)
	
res = []
powerSet(list("abcdefg"), [], 0, res)
print res