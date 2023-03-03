#Input two Sets from User and find the common elements between them without using
#any inbuilt function.
s1=set()
s3=set()
size=int(input("Enter the size of set1: "))
for i in range(0,size):
    var=input("Insert Element: ")
    s1.add(var)
s2=set()
size=int(input("Enter the size of set2: "))
for i in range(0,size):
    var=input("Insert Element: ")
    s2.add(var)
print(s1)
print(s2)
for i in s1:
    for j in s2:
        if (i==j):
            s3.add(i)
if(len(s3)==0):
    print("There is no any common element in set 1 and set2 ")
else:
    print("Common element from set 1 and set 2 are:",s3)