def generate_permutations(string, chosen):
	# print "calling permutate for (", string, " , ", chosen, ")" 
	if len(string) == 0:
		print chosen
		return
	else:
		for i in range(len(string)):
			chosen += string[i]
			temp = string[i] 
			string.remove(temp)
			generate_permutations(string, chosen)
			chosen.pop(len(chosen)-1)
			string.insert(i, temp)
	

generate_permutations(list("abcd"), [])