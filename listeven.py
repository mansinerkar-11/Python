l1=[]
l1size=0
l1size=int(input("enter the size of list: "))
print("enter the elements of list ")
for i in range(0,l1size):
    val=int(input("element : "))
    l1.append(val)
for i in range(0,l1size):
    if(l1[i]%2==0):
        print(l1[i])
