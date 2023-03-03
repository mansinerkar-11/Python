#print the number in words for Example: 1234 => One Two Three Four

num1 = int(input("Enter any number:"))
t1 = tuple() 
while num1 > 0:
    words = num1 %10
    if words == 0: 
        t1=t1+("Zero",)
    elif words == 1:
        t1=t1+("One",)
    elif words == 2:
        t1=t1+("Two",)
    elif words == 3:
        t1=t1+("Three",)
    elif words == 4:
        t1=t1+("Four",)
    elif words == 5:
        t1=t1+("Five",)
    elif words == 6:
        t1=t1+("Six",)
    elif words == 7:
        t1=t1+("Seven",)
    elif words == 8:
        t1=t1+("Eight",)
    elif words == 9:
        t1=t1+("Nine",)
    num1 = num1 // 10
for i in range(len(t1)-1,-1,-1):
    print(t1[i],end=" ")