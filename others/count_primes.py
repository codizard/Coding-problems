def countPrimes(n):
	primes = [True for i in range(0, n)]
	p = 2
	i = 2
	cp = 2
	ci = 2
	while p <n:
		if primes[p] is True:
			while i <n:
				if i == p:
					i+= p
				else:
					primes[i] = False
					i+=p
		ci+=1
		cp+=1
		p = cp
		i = ci

	for i in range(2, len(primes)):
		if primes[i]:
			print i,

countPrimes(10)