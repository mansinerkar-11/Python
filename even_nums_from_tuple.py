#Write a python program to input the values from user and insert them into a tuple
#and display the all even numbers
t1=()
t1size=0
t1size=int(input("enter the size of list: "))
for i in range(0,t1size):
    val=int(input("Element: "))
    t1=t1+(val,)
print("Even Numbers")
for i in t1:
    if(i%2==0):
        print(i)


