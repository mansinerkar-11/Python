#Q2. Write a Python program to find the repeated items of a tuple.
# Input a tuple from User.
tup1=()
tup2=()
size=int(input("Enter the size of tuple: "))
for i in range(0,size):
    val=int(input("Enter the Element: "))
    tup1+=(val,)
print("The Elements of tuple are:",tup1)
print("Repeated elements in tuple")
for i in range(0,size):
    for j in range(i+1,size):
        if(tup1[i]==tup1[j]):
            print(tup1[j],end="")

            

