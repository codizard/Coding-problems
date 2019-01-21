import heapq

def one_away(word1, word2):
	changes = 0
	for i in range(len(word1)):
		if word1[i] != word2[i]:
			changes +=1
	return changes == 1
 
def find_closest_words(word, wordList):
	res = []
	for x in wordList:
		if one_away(x, word):
			res.append(x)
	return res
def shortest_transformation(bw, ew, wl):
	res = []
	stack = []
	if ew not in wl:
		return 0
	stack= [(ew, 1)]
	if one_away(ew, bw):
		return 2
	wl.remove(ew)
	while stack:
		# print "The stack is ", stack
		cur, count= stack.pop(0)
		if one_away(cur, bw):
			# heapq.heappush(res,(count+1, cur))
			return count+1
		closest_words = find_closest_words(cur, wl)
		for closest_word in closest_words:
			stack.append((closest_word, count+1))
			wl.remove(closest_word)	
	if len(res) > 0:
		return res[0][0]
	return 0

wl = ["qit", "qot","dot","dog","lot","log","hog","fog","zog","qog","cog"] 
ew= "cog"
bw = "hit"
print shortest_transformation(bw, ew, wl)
