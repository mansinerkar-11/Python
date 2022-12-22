#Print the number in words for Example: 1234 => One Two Three Four.
# Input a tuple from User.
num=int(input("Enter Number: "))
t1=()
while num>0:
    words=num%10
    if words==0:
        t1=t1+("Zero ",)
    elif words==1:
        t1+=("One ",)
    elif words==2:
        t1+=("Two ",)
    elif words==3:
        t1+=("Three ",)
    elif words==4:
        t1+=("Four ",)
    elif words==5:
        t1+=("Five ",)
    elif words==6:
        t1+=("Six ",)
    elif words==7:
        t1+=("Seven ",)
    elif words==8:
        t1+=("Eight ",)
    elif words==9:
        t1+=("Nine ",)
    num//=10
for i in range(len(t1)-1,-1,-1):
    print(t1[i],end="")
    
