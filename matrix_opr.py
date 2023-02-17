# Write a Python program to compute following computation on matrix:
# a)  Addition of two matrices	
# B) Subtraction of two matrices 
# c) Multiplication of two matrices 
# d) Transpose of a matrix
print("------------Information of matrix 1------------")
r1=int(input("\nHow many rows do you want in matrix: "))
c1=int(input("How many columns do you want in matrix: "))
matrix1=[]
print("Enter the elements rowise: ")
for i in range(r1):
    m1=[]
    for j in range(c1):
        ele=int(input())
        m1.append(ele)
    matrix1.append(m1)
    
for i in range (r1):
    print("\n")
    for j in range (c1):
        print(matrix1[i][j] , end="  ")
        

print("\n------------Information of matrix 2------------")
r2=int(input("\nHow many rows do you want in matrix: "))
c2=int(input("How many columns do you want in matrix: "))
matrix2=[]
print("Enter the elements rowise: ")
for i in range(r2):
    m2=[]
    for j in range(c2):
        ele=int(input())
        m2.append(ele)
    matrix2.append(m2)
    
for i in range (r2):
    print("\n")
    for j in range (c2):
        print(matrix2[i][j] , end="  ")
        


def addition():
    if(r1==r2 and c1==c2):
        add=[]
        for i in range (r1):
            r=[]
            for j in range(c1):
                a=matrix1[i][j] + matrix2[i][j]
                r.append(a)
            add.append(r)
            
        for i in range (r1):
            print("\n")
            for j in range (c1):
                print(add[i][j] , end="  ")
    else:
        print("Addition cannot be performed")
            
def subtraction():
    
    if(r1==r2 and c1==c2):
        sub=[]
        for i in range (r1):
            r=[]
            for j in range(c1):
                a=matrix1[i][j] - matrix2[i][j]
                r.append(a)
            sub.append(r)
            
        for i in range (r1):
            print("\n")
            for j in range (c1):
                print(sub[i][j] , end="  ")
                
    else:
        print("Subtraction cannot be performed")
            
            
def multiplication():
    
    
    if(r2==c1):
        multi=[]
        for i in range (r1):
            r=[]
            for j in range(c2):
                a=0
                for k in range (c1):
                    a+=matrix1[i][j] * matrix2[i][j]
                    r.append(a)
            multi.append(r)
            
        for i in range (r1):
            print("\n")
            for j in range (c1):
                print(multi[i][j] , end="  ")
                
    else:
        print("Multiplication cannot be performed")
            
def transpose():
    trans=[]
    
    for i in range (r1):
        r=[]
        for j in range(c1):
            r.append(0)
        trans.append(r)
        
    for i in range (r1):
        for j in range(c1):
            trans[i][j]=matrix2[j][i]
            
    for i in range (r1):
        print("\n")
        for j in range (c1):
            print(trans[i][j] , end="  ")        
        

def mainf():
    print("____________________________________________________\n")
    print("\n1)  Addition of two matrices	\n2) Subtraction of two matrices \n3) Multiplication of two matrices \n4) Transpose of a matrix")
    ch=int(input("Enter Your choice: "))
    if(ch==1):
        print("Addition of two matrices")
        addition()
    elif(ch==2):
        print("Subtraction of two matrices")
        subtraction()
    elif(ch==3):
        print("Multiplication of two matrices")
        multiplication()
    elif(ch==4):
        print("Transpose of a matrix")
        transpose()
    else:
        print("Invalid choice........!!!")
    
def ask():
    yn=input("\nDo you want to continue(y/n): ")
    if(yn=='Y' or yn=='y'):
        mainf()   
        ask()
    else:
        exit()
    
mainf()
ask()
