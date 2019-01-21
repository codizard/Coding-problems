def minimum_window(s, t):
	t_map = {}
	s_map = {}
	words_seen = 0
	words_required = len(set(t))
	minLen = float('inf')
	start, end = 0, 0
	for x in t:
		if x not in t_map:
			t_map[x] = 1
		else:
			t_map[x] +=1

	while end < len(s):
		char = s[end]
		if char in s_map:
			s_map[char] +=1
		else:
			s_map[char] = 1
		if char in t_map and s_map[char] == t_map[char]:
			words_seen +=1

		while start < end and words_seen == words_required:
			st_char = s[start]
			if end - start + 1 < minLen:
				minLen = end - start + 1
				startPos = start
				endPos = end
			start +=1
			s_map[st_char] -=1

			if st_char in t_map and s_map[st_char] < t_map[st_char]:
				words_seen-=1

		end+=1
	if minLen == float('inf'):
		return ""
	return s[startPos : endPos + 1]
		

print minimum_window("abaapcbpab", "abc")