def edit_distance(s1, s2, m, n, memo):
	print "edit_distance for ", s1[m-1], s2[n-1]
	if not m:
		return n	
	if not n:
		return m

	if s1[m-1] == s2[n-1]:
		return edit_distance(s1, s2, m-1, n-1, memo)

	if (s1, s2) not in memo and (s2, s1) not in memo:
		memo[(s1, s2)] = 1 + min( edit_distance(s1, s2, m, n-1, memo),
					edit_distance(s1, s2, m-1, n, memo),
					edit_distance(s1,s2, m-1, n-1, memo)
				)
	return memo[(s1, s2)]


s1 = "bridge"
s2 = "ebridg"
print edit_distance(s1, s2, len(s1), len(s2), {})