print("Information for matrix1")

r1=int(input("Enter the number of rows for matrix1:"))
c1=int(input("Enter the number of columns for matrix1:"))

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
    
print("Information for matrix2")
r2=int(input("\nEnter the number of rows for matrix1:"))
c2=int(input("Enter the number of columns for matrix1:"))


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
            
            
ch=0
while(ch!=5):

    print("Enter your choice: ")
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Transpose \n5. Exit")
    ch=int(input())
    
    if(ch==1):
       addition() 
       
    elif(ch==2):
        subtraction()
    
    elif(ch==3):
        multiplication() 
        
    elif(ch==4):
        transpose()
         
    elif(ch==5):
        break;
        
