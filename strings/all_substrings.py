def generate_all_substrings(string):
	for i in range(len(string)-1):
		for j in range(i, len(string)):
			print string[i:j+1]
	pass

generate_all_substrings("abcde")