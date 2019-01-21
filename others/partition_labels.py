'''
a b a b c b a b 

i
			j
'''

def partition_labels(string):
	lastMap = {}
	for i in range(len(string)):
		lastMap[string[i]] = i
	i = 0
	j = 0
	res = []
	while i < len(string) and j < len(string):
		j = lastMap[string[i]]
		while i <= j:
			last = lastMap[string[i]]
			if last > j:
				j = last
			i+=1
		res.append(j-i)

	print res


partition_labels("ababcbacadefegdehijhklij")