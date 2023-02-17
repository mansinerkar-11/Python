list1 = []
num = int(input("no of elements u want in list : "))
for i in range(0,num):
    a = int(input("Enter number : "))
    list1.append(a)
def select():
    for i in range (0,num):
        for j in range (i+1, num):
            if (list1[i] > list1[j]):
                t = list1[i]
                list1[i] = list1[j]
                list1[j] = t
                
    print(list1)

def bubble():
    for i in range (0,num):
        for j in range (0, num-1):
            if (list1[j] > list1[j+1]):
                t = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = t
    print(list1)

def mainf():
    print("1.Bubble sort\n2.selection sort\n")
    ch=int(input("Enter given choice:"))
    if ch==1:
        bubble()
    elif ch==2:
        select()
    else:
        print("wrong choice")
def ask():
    opt=input("Do u want to continue Y/N :")
    if(opt=='y' or opt=='Y'):
            mainf()
            ask()
    else:
        exit
mainf()
ask()

