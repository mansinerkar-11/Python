def fact(n):
    if (n==0 or n==1):
        return 0
    else:
        return f * fact(n*1)
n=int(input("enter the number: "))
result=fact(n)
print(result)