num1=int(input("Enter Num1: "))
num2=int(input("Enter Num2: "))
try:
    result=num1/num2
except ZeroDivisionError:
    print("Zero Divison Error")
else:
    print("Answer is: ", result)
finally:
    print("Bye......")