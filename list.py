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
count = pd.Series(l2).value_counts()
print("Element Count")
print(count)


print("No. of absent students: ", absent)
avg = total/n
print("Avg marks = ",avg)	
print("Min",min(l2))	
print("Max",max(l1))	
