#Write a Python program to find the repeated items of a tuple.
t1=()
sizet1=int(input("Enter the size: "))
for i in range(0,sizet1):
    val=int(input("Element: "))
    t1=t1+(val,)
print(t1)
print("Repeated elements in tuple")
for i in range(0,sizet1):
    for j in range(i+1,sizet1):
        if(t1[i]==t1[j]):
            print(t1[j],end="")