def powerSet(string):
	n = len(string)
	poss = pow(2,n)
	for i in range(poss):
		for j in range(n):
			if i & (1 << j):
				print string[j],
		print ""

	pass

powerSet("abc")