
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter The Number: "))
res=fact(n)
print("factorial of ",n,"is ",res)
