def recursive_multiply(n1, newn1, n2):
	print "recursive_multiply (", newn1, " ", n2, ")"
	if n2 == 1:
		print newn1
	else:
		recursive_multiply(n1, newn1 + n1, n2-1)

def rec(n1, n2):
	if n2 > n1:
		n1, n2 = n2, n1
	recursive_multiply(n1, n2)

recursive_multiply(20, 20,  10)