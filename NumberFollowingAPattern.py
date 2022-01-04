#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        seq=S
        n = len(seq)
 
        if (n >= 9):
            return "-1"
     
        result = [None] * (n + 1)
     
        count = 1
     
        # The loop runs for each input character
        # as well as one additional time for
        # assigning rank to remaining characters
        for i in range(n + 1):
            if (i == n or seq[i] == 'I'):
                for j in range(i - 1, -2, -1):
                    result[j + 1] = int('0' + str(count))
                    count += 1
                    if(j >= 0 and seq[j] == 'I'):
                        break
        ans=""
        for i in result:
            ans=ans+str(i)
        return(int(ans))

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends
