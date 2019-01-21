def edit_distance_helper(s1, s2, m, n, cost):
	if m == 0:
		return n
	if n == 0:
		return m
	if s1[m-1] == s2[n-1]:
		return edit_distance_helper(s1, s2, m-1, n-1, cost)
	else:
		if (s1, s2) not in cost and (s2, s1) not in cost:
			return 1 + min(
				edit_distance_helper(s1, s2, m, n-1, cost),
				edit_distance_helper(s1 , s2, m-1, n, cost),
				edit_distance_helper(s1, s2, m-1, n-1, cost)
				)
			return cost[(s1, s2)]
		else:
			return cost[(s1, s2)]

def edit_distance(s1, s2):
	cost = {}
	return edit_distance_helper(s1, s2, len(s1), len(s2), cost)

print edit_distance("horse", "ros")
