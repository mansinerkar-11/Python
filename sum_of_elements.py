#Q1. Write a python program to find the sum of all elements, largest element and smallest
#element from the tuple input tuple from user
tup1=()
size=int(input("Enter the size of tuple: "))
for i in range(0,size):
    var=int(input("Enter the Element: "))
    tup1+=(var,)
print("The sum of all elements: ",sum(tup1))
print("The largest elements: ",max(tup1))
print("The smallest elements: ",min(tup1))