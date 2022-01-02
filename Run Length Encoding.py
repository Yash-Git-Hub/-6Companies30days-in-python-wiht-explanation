#Your task is to complete this function
#Function should return complete string
def encode(arr):
    ans=''
    count=1
    char=''
    for i in arr:
        if(char==i):
            count=count+1
        else:
            ans=ans+str(count)
            count=1
            char=i
            ans=ans+char
    ans=ans+str(count)
    return(ans[1:])
#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
