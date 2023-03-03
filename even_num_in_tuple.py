#Write a Python program to display Even numbers from a tuple. Input a tuple from User.
tup=()
even=()
size=int(input("Enter The Size Of Tuple: "))
for i in range(0,size):
    var=int(input("Enter Element: "))
    tup+=(var,)
print("Your Tuple is:",tup)
for i in tup:
    if(i%2==0):
        even+=(i,)
print("Even Number from tuple is:",even)
