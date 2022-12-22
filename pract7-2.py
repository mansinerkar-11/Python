#write a python program to input a tuple and display the sum of all the values in tuple and
#largest and smallest number from the tuple
t1=()
t1size=0
t1size=int(input("enter the size of list: "))
for i in range(0,t1size):
    val=int(input("Element: "))
    t1=t1+(val,)
print(t1)
print("sum of all elements: ",sum(t1))
print("Largest number in tuple: ",max(t1))
print("smallest number in tuple: ",min(t1))


