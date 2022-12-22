t1=()
t1size=0
t1size=int(input("enter the size of list: "))

print("enter elements of tuple: ")
for i in range(0,t1size):
    val=int(input(":"))
    t1=t1+(val,)
print("Even Numbers")
for i in t1:
    if(i%2==0):
        print(i)

