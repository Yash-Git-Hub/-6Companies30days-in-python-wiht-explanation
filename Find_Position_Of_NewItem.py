#User function Template for python3

class Solution:
    def findPosition(self, N , M , K):
    # n - k + 1 is number of positions
    # before we reach beginning of circle
    # If m is less than this value, then
    # we can simply return (m-1)th position
        m=M
        n=N
        k=K
        if (m <= n - k + 1):
           return m + k - 1
      
        # Let us compute remaining items before
        # we reach beginning.
        m = m - (n - k + 1)
      
        # We compute m % n to skip all complete
        # rounds. If we reach end, we return n
        # else we return m % n
        if(m % n == 0):
            return n
        else:
            return m % n
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M,K=map(int,input().split())
        
        ob = Solution()
        print(ob.findPosition(N,M,K))
# } Driver Code Ends
