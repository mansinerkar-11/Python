num=int(input("Enter Number: "))
try:
    if(num<0):
        raise exception
except:
    print("The number is less than zero")
else:
    print("The number is ", num)
finally:
    print("Bye..")