s1=set()
size=int(input("Enter the size: "))
for i in range(0,size):
    var=input("Enter Element: ")
    s1.add(var)
print(s1)
update1=input("Do you want to update more elements in set y/n: ")
if ((update1=="y")):
    sizeadd=int(input("Enter how many element you want to add: "))
    print("enter element for updating set")
    for i in range(0,sizeadd):
        var2=input("Enter element: ")
        #using add method
        #s1.add(var2)  
        #usin update method
        s1.update([var2])
    print(s1)
else:
    print("Thank you...!")
print("This is set: ",s1)
rmv=input("Enter what you want to remove: ")
if rmv in s1:
    s1.remove(rmv)
    print(s1)
else:
    print("using discard")
    s1.discard(rmv)

