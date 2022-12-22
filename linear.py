n = int(input("Enter no. of elements"))
a = []
for i in range (n):
	ele = int(input("Enter element:"))
	a.append(ele)
num = int(input("Enter no. to be searched in the list"))
flag =0
for i in range(n):
	if num == a[i]:
		print("Element found at",i)
		flag =1
		break
if flag==0:
	print("Element not found")	
