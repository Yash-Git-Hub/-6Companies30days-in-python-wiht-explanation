
class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        key=k
        arr=a
        temp,count,res=0,0,1
        for j in range(n):
            for k in range(temp,n):
                res*=arr[k]
                if res>=key:
                    res/=arr[k]
                    break
            else:
                k=n
            count+=(k-j)
            res=(res/(arr[j]))
            temp=k
            if k-j==0:
                res=1
                temp=k+1
        return(count)
        
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1
