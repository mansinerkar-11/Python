t1=()
t1size=0
t1size=int(input("enter the size of list: "))
for i in range(0,t1size):
    t1=t1+(i,)
for i in t1:
    if(i%2==0):
        print(i)

