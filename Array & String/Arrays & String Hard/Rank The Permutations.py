class Solution:
	def findRank(self, s):
		# code here
		n = len(s)
		fact = [1] *(n + 1)
		for i in range(1, n + 1):
		    fact[i] = fact[i-1] * i
		rank = 1
		for i in range(n):
		    smaller = 0
		    for j in range(i + 1,n):
		        if s[j] < s[i]:
		            smaller += 1
		    rank += smaller * fact[n - i - 1]
		return rank