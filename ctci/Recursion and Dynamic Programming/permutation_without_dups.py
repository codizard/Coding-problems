def permutation_without_dups(string, chosen):
	if len(string) == 0:
		print chosen
		return None
	else:
		for i in range(len(string)):
			chosen.append(string[i])
			temp = string[i] 
			string.pop(i)
			permutation_without_dups(string, chosen)
			string.insert(i,temp)
			chosen.pop(len(chosen)-1)

a = "abc"
# print list(a)
permutation_without_dups(list(a), [])