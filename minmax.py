import pandas as pd
l1 = []
l2 = []
absent = 0
n =0
total = 0

a = int(input("Enter no. of students to be added:"))
for i in range(a):
	ele = int(input("Enter marks(Enter -1 for absentees):"))
	l1.append(ele)
print(l1)
for y in l1:
	if y == -1:
		absent+=1
	elif y != -1:
		total +=y
		n +=1
		l2.append(y)
mini = l2[0]
for j in range(1,len(l2)):
	if mini<l2[j]:
		pass
	else:
		mini = l2[j]
print("Minimum marks",mini)

maxi = l2[0]
for k in range(1,len(l2)):
	if maxi>l2[k]:
		pass
	else:
		maxi = l2[k]
print("MAx Marks",maxi)

count2 = 0
for y in range(0,len(l2)):
	for m in range(0,len(l2)):
		if l2[y] == l2[m]:
			count2+=1
	print("Element",l2[y],"occurs",count2,"times")

	
			
print("No. of absent students: ", absent)
avg = total/n
print("Avg marks = ",avg)	

