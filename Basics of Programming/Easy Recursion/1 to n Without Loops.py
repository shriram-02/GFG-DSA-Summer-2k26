class Solution:
    def printTillN(self, n):
    	#code here 
    	if n == 0:
    	    return 
        self.printTillN(n-1)
        print(n,end = " ")