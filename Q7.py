#Write a Python program to find maximum and the minimum value in a set
# and to find the length of a set.
s1=set()
size=int(input("Enter the size of set: "))
for i in range(0,size):
    var=input("Insert Element: ")
    s1.add(var)
print("set: ",s1)
print("The minimum value in set is: ",min(s1))
print("The maximum value in set is: ",max(s1))
print("Length of your set is: ",len(s1))