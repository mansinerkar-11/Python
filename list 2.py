rows=4
k=0*rows-5   
for i in range(rows,-2,-2):   
    for j in range(k,0,-1):  
        print(end=" ")   
    k=k+1   
    for j in range(0,i+1):  
        print("*",end="")  
    print("")

    