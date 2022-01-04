#User function Template for python3
import itertools
class Solution:
	def CountWays(self, str):
	    count=0
        for i in (range(len(str))):
            if(int(str[i])==0):
                if(i-1>0):
    	            if(int(str[i-1])>2 or int(str[i-1])<=0):
    	                return(0)
    	            else:
    	                pass
    	        else:
    	            return(0)
	    for i in range(len(str)-1,-1,-1):
	        if(int(str[i])!=0):
	            count=count+1
	        if(i-1>=0):
    	        if(int(str[i])<7 and int(str[i-1])<2):
    	            count=count+1
		return(count-1)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.CountWays(str)
		print(ans)

# } Driver Code Ends
