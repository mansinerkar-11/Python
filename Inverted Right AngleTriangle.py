#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

def invTriangleWall(s):
    
    
    #Complete the given code
    #Replace .... by your own code
    for i in range(s):
        for j in range(s-i):
            print("* ",end="")
        print()
    

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        s=int(input())
        invTriangleWall(s)
# } Driver Code Ends
