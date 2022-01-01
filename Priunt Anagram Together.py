#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        owords=words.copy()
        for i in range(len(words)):
            xx=sorted(words[i])
            words[i]="".join(xx)
        x=set(words)
        d={}
        for i in x:
            d[i]=[]
            
        for i in range(len(words)):
            d[words[i]].append(i)
        ans=[]
        
        for i in d.keys():
            w=[]
            for j in d[i]:
                w.append(owords[j])
            ans.append(w)
        return(ans)
            
            
        
        
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
