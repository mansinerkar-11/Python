"""Practical No 4        Roll No.: 77         class:SE-B
a) Write a Python program to store names and mobile numbers of your friends in sorted order on names. 
Search your friend from list using binary search (recursive and non- recursive). 
Insert friend if not present in phonebook
b) Write a Python program to store names and mobile numbers of your friends in sorted order on names. 
Search your friend from list using Fibonacci/Linear search. Insert friend if not present in phonebook.
"""
#Binary Search 

name=[]
number=[]
n=int(input("Enter the number of entries to store :"))

for i in range(0,n):
    name_input=input("Enter Name:")
    mob_input=input("Enter Mobile Number:")
    name.append(name_input)
    number.append(mob_input)

print("Friend Details Stored in PhoneBook are :")
print(name)
print(number)

def Sorting(name,number,n):
    for i in range(0,n):
        for j in range(0,n-1):
            if (name[j]>name[j+1]):
                t=name[j]
                name[j]=name[j+1]
                name[j+1]=t

def BinarySearch(list1, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if list1[mid] == x:
            return mid
        elif list1[mid] > x:
            return BinarySearch(list1, low, mid - 1, x)

        elif list1[mid] < x:
            return BinarySearch(list1, mid + 1, high, x)
 
    else:
        return -1
    

def AddNew(n,name,x,number):
    n+=1
    name.append(x)
    b=int(input("Enter friend's number:"))
    number.append(b)
    

def Search(name,number,n):
    y=input("Enter name to search :")
    result = BinarySearch(name, 0, len(name)-1, y)
    if result != -1:
        print("Friend is present at position:", str(result)+1)
    else:
        print("Friend is not present in phonebook:")
        charr=input("Do you want to add number in phonebook(Y/N):")
        while charr=='Y' or charr=='y':
            AddNew(n,name,y,number)
            break;
    
Sorting(name, number, n)
Search(name, number, n)
print("------------------------------------------------------------------------------\n")
print("Friend Details Stored in PhoneBook are :")
print(name)
print(number)