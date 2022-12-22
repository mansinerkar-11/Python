t1=()
num=0
sizet1=int(input("Enter size of tuple: "))
for i in range(0,sizet1):
    var=input("Enter element in tuple: ")
    t1=t1+(var,)
print("t1=",t1)
print("Enter the element to check: ")
var2=int(input("Enter element: "))
t2=t1.count(var2)
print(t2)

print("Enter the element to find the index: ")
var3=int(input("Enter element: "))
print(t1.index(var3))
