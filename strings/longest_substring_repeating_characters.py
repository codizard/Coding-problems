def longest_substring_without_repeating_characters(string):
	visited = set()
	length = 0
	i = 0
	j = 0
	while i < len(string):
		if string[i] not in visited:
			visited.add(string[i])
			i+=1

			if i-j > length:
				length = i - j
		else:
			visited.remove(string[j])
			j+=1

	return length

print longest_substring_without_repeating_characters("abcdpb")