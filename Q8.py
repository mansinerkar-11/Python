# Write a Python program to Input elements in the Set and find out only Even Numbers
#from Set and Display.
print("Even Numbers")
s1=set()
s2=set()
size=int(input("Enter the size of set: "))
for i in range(0,size):
    var=int(input("Insert Element: "))
    s1.add(var)
for i in s1:
    if (i%2==0):
        s2.add(i)
if(len(s2)==0):
    print("No even numbers are available in set")
else:
    print("Even number from set: ",s2)


