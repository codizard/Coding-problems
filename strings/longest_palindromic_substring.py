'''
k = 3
a b b c c 
    i   j
[

T F F F F
F T T F F
F F T F F
F F F T T
F F F F T
]
   

'''

def longest_palindromic_substring(string):
	dp = [[False for i in range(len(string))] for j in range(len(string))]
	m = len(dp)
	n = len(dp[0])
	maxLen = 1
	#gen len 1 palindromic substrings

	for i in range(m):
		for j in range(n):
			if i == j:
				dp[i][j] = True
				startIndex = i
    #gen len 2 palindromic substrings
	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			dp[i][i+1] = True
			maxLen = 2
    		startIndex = i 
	for k in range(3, len(string)+1):
		for i in range(0, len(string)-k+1):
			j = i + k - 1
			if string[i] == string[j] and dp[i+1][j-1] is True:
				dp[i][j] = True
				if k > maxLen:
					maxLen = k
					startIndex = i
	return string[startIndex:maxLen+1]




# print longest_palindromic_substring("abbbbbbbbbc") == 9
# print longest_palindromic_substring("abcblkabak") == 5
print longest_palindromic_substring("aba")
# print longest_palindromic_substring("ab") == 1