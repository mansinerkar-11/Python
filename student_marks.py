# Write a Python program to store marks scored in subject “Fundamental of Data Structure” by 
# N students in the class. Write functions to compute following:
# a)	The average score of class
# b)	Highest score and lowest score of class
# c)	Count of students who were absent for the test
# d)	Display mark with highest frequency

#accept student information
import statistics
student=[]
total=0
present=0
present_student_marks=[]
absent=0
size=int(input("Enter total number of students: "))
print("***Note:If student is absent then enter their marks -1 else put marks outof 100 nagetive marking will consider as absent***")
temp=0
while(temp<size):
    val=int(input("Enter student marks: "))
    if(val<=100):
        student.append(val)
        temp+=1
    else:
        print("Invalid marks...! please enter marks out off 100")
        
# find absent and present
for j in student:
    if(j>=0):
        present+=1
        total+=j
        present_student_marks.append(j)
    else:
        absent+=1

def high(h):
    return max(h)
def low(l):
    return min(l)
def occ(oc):
    res = statistics.mode(present_student_marks)
    return res

print("The average score of class: ",(total/size))
print("Highest score of class is: ",high(student),"\nLowest score of class is: ",low(present_student_marks))
print("students who were absent for the test: ",absent)
print("Marks with highest frequency",occ(present_student_marks))


