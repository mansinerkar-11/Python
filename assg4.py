"""Practical No 4        Roll No.: 77         class:SE-B
a) Write a Python program to store names and mobile numbers of your friends in sorted order on names. Search your friend from 
list using binary search (recursive and non- recursive). Insert friend if not present in phonebook
b) Write a Python program to store names and mobile numbers of your friends in sorted order on names. Search your friend from list using Fibonacci/Linear search. Insert friend if not present in phonebook.
"""

list1=[]
list2=[]
a=int(input("Enter number of entries u want to store:"))

for i in range(0,a):
    name=input("Enter name:")
    mob=input("Enter mob:")
    list1.append(name)
    list2.append(mob)
print(list1)
print(list2)
for i in range(0,a):
    for j in range(0,a-1):
        if (list1[j]>list1[j+1]):
            t=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=t
            
for i in range(0,a):
    print("Name:",list1[i])

def binary_search(lst, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, low, mid - 1, x)

        else:
            return binary_search(lst, mid + 1, high, x)
 
    else:
        return -1
def addnumname(a,list1,x,list2):
    a+=1
    list1.append(x)
    b=int(input("Enter friend's number:"))
    list2.append(b)
    for i in range(0,a):
        print("Name:",list1[i],"Number:",list2[i])

    
def mainfun():
    y=input("Enter name to search:")
    result = binary_search(list1, 0, len(list1)-1, y)
    if result != -1:
        print("friend is present at position:", str(result)+1)
    else:
        print("friend is not present in phonebook:")
        charr=input("Do u want to add number in phonebook:Y/N")
        while charr=='Y' or charr=='y':
            addnumname(a,list1,y,list2)
            break;

ask=input("do you want to search more name's:Y/N")
while ask=='Y' or ask=='y':
    mainfun()
'''
Enter number of entries u want to store:3           
Enter name:sdf
Enter mob:1234567890
Enter name:mjgd
Enter mob:3456789012
Enter name:zhhjas
Enter mob:5674389201
['sdf', 'mjgd', 'zhhjas']
['1234567890', '3456789012', '5674389201']
Name: mjgd
Name: sdf
Name: zhhjas
do you want to search more name's:Y/Nn
'''
