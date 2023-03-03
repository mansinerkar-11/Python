list_1=[]
list_2=[]
absent=0
present=0
total=0
n=0
def hig(h):
    n=0
    for i in h:
        if(i>n):
            n=i
    return n

def low(l):
    n=100
    for i in l:
        if(i<n):
            n=i
    return n
a=int(input("Enter no. of students :"))
for i in range(a):
	b=int(input("enter marks out of 100(Enter -1 for absentess):"))
	list_1.append(b)
print(list_1) 
for y in list_1:
	if y== -1:
		absent+=1
	elif y!= -1:
		present+=1
		total+=y
		n+=1
		list_2.append(y)
marks_occ=int(input("enter mark which occur:"))		
occur=0
for i in list_2:
	if i==marks_occ:
		occur+=1
print(occur)
occur_1={}
for i in list_2:
	if i in occur_1:
		occur+=1
		
print("Avg score of class:",total/n)
print("Highest marks of class:",hig(list_2),"Lowest marks of class:",low(list_2))
print("Number of absent student:",absent)
def countocc(c):
    dictn={}
    for i in c:
        occr_s=0
        for j in c:
            if (i==j):
                occr_s+=1
        dictn[i]=occr_s
    # print(dictn)
    # print(dictn.values())
    n=0
    for i in dictn.values():
        if i>n:
            n=i
    for key, value in dictn.items():
            if n == value:
                print (key) 

higfirq=countocc(list_2)
print("marks with highest frequency",higfirq)
