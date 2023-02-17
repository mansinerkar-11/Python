# Write a Python program to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using
# a)	Insertion sort
# b)	Shell Sort and display top five scores
from math import floor
marks=[]
size=int(input("How many student`s data do you want to add: "))

temp=0
while(temp<size):
    val=int(input("Enter marks: "))
    if(val<=100):
        marks.append(val)
        temp+=1
    else:
        print("Enter marks outof 100")

def InsertionSort():
    for i in range(0,size):
        index = marks[i]
        j = i-1
        while j>=0 and index<marks[j]:
            marks[j+1]=marks[j]
            j-=1
            marks[j+1]=index
    print(marks)
       
def ShellSort():
    gap=floor(size/2)
    while gap>0:
        for i in range(0,size):
            temp=marks[i]
            j=i
    while j >= gap and marks[j-gap] >temp:
        marks[j] = marks[j-gap]
        j -= gap
        marks[j] = temp
        gap = floor(gap/2)
    print(marks)

def top():
    n=5
    print("Top 5 students are : ",marks[-n: ])

        
def mainf():
    print("1. Insertion Sort and display top five scores \n2. Shell sort and display top five scores")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print("1. Insertion Sort and top five scores")
        InsertionSort()
        top()
    elif(ch==2):
        print("Shell sort and top five scores")
        ShellSort()
        top()
    else:
        print("Invalid choice....!")

def ask():
    asking=input("Do you want to contineu(y/n): ")
    if(asking=='y' or asking=='Y'):
        mainf()
        ask()
    else:
        exit()            
mainf()
ask()