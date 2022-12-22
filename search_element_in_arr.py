# Given an integer array and another integer element. The task is to find if the given element is present in array or not.

import math
class Solution:
    def search(self,arr, N, X):
        if X in arr:
            return arr.index(X)
        else:
            return -1  
def main():
        T=int(input())
        while(T>0):
            
            N=int(input())
            
            A=[int(x) for x in input().strip().split()]
            
            x=int(input())
            ob=Solution()
            print(ob.search(A,N,x))
            
            T-=1
