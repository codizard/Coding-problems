'''
caab
ca.*cb

'''

def pattern_matching(string, pattern):
	#edge cases
	i = len(string) - 1
	j = len(pattern) - 1

	while i >= 0 and j >= 0:
		if string[i] == pattern[j]:
			i-=1
			j-=1
		else:
			if pattern[j] == ".":
				i-=1
				j-=1
			elif pattern[j] == "*":
				if j > 0 and pattern[j-1] not in ["*", "."]:
					if pattern[j-1] ==  string[i]:
						j-=2
						temp = string[i]
						while string[i] == temp:
							i-=1
					else:
						return False 
				elif j > 0 and pattern[j-1] == ".":
					if len(string)>=j-1 and pattern[:j-1] == string[:j-1]:
						return True
					else:
						return False
			else:
				return False

	while i > 0:
		return False
	while j > 0:
		pass	
		#parse the string to check * alternates a char or (.)
	return True

print pattern_matching("caaaaaaaaaaab", "cb.*b")