try:
    num1=int(input("Enter the 1st number: "))
    num2=int(input("Enter the 2nd number: "))
    print("num1 divided by num2: ",num1/num2)
except ZeroDivisionError:
    print("Error....Number cannot divided by zero")
finally:
    print("Bye...")