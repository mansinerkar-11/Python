#Write a Python program to create a set,
#add member(s) in a set and remove one item from set.
s1=set()
size=int(input("Enter the size of set: "))
for i in range(0,size):
    var=input("Enter The Element: ")
    s1.add(var)
print("Your set is: ",s1)
rem=input("Enter Which Element you want to remove: ")
if rem in s1:
    s1.remove(rem)
    print("Element removed sucessfullyyy...!")
    print("Your set after Removing the element: ",s1)
else:
    print("Element is not available in set.......!")