# Write a Python program to store first year percentage of students in array. Write function for 
# sorting array of floating point numbers in ascending order using
# a)	Selection Sort
# b)	Bubble sort and display top five scores.

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

def selection():
    for i in range(0,size):
        for j in range(i+1, size):
            if(marks[i]>marks[j]):
                marks[i],marks[j]=marks[j],marks[i]
    print("Your sorted list using selection sort is: ",marks)


def bubble():
    for i in range(size):
        for j in range(0,size-i-1):
            if(marks[j]>marks[j+1]):
                marks[j],marks[j+1]=marks[j+1],marks[j]
    print("Your sorted list using bubble sort is: ", marks)
    
      
def top():
    n=5
    print("Top 5 students are: ",marks[-n:])             
            
def mainf():
    print("1. Selection Sort and display top five scores \n2. Bubble sort and display top five scores.")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print("1. Selection Sort and top five scores")
        selection()
        top()
    elif(ch==2):
        print("Bubble sort and top five scores")
        bubble()
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