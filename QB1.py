# #Program to display 1 to 10 even odd number
# num=10
# for i in range(1,num+1):
#     if (i%2==0):
#         print("Even Number:",i)
#     else:
#         print("Odd Number: ",i)
# # #Program to print 1 to 10 reverse number
# for i in range(10,0,-1):
#     print(i)
#Print common item from 2 list
# l1=[]
# size=int(input("Enter the size of L1: "))
# for i in range (0,size):
#     var=input("Enter Element: ")
#     l1.append(var)
# l2=[]
# size=int(input("Enter the size of L2: "))
# for i in range (0,size):
#     var1=input("Enter Element: ")
#     l2.append(var1)
# print("l1=",l1)
# print("l2=",l2)
# l3=[]
# for i in l1:
#     for j in l2:
#         if (i==j):
#             l3.append(i)
# print("Common item L1 and L2 : ",l3)

d1={}
size=int(input("Enter the size: "))
for i in range(0,size):
    key=input("Enter Key: ")
    value=input("Enter Value: ")
    d1[key]=value
print(d1)

    