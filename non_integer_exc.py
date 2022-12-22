try:
    num=int(input("Enter integer: "))
except ValueError:
    print("Error....you have entered non integer value")
else:
    print("Entered number is: ",num)
finally:
    print("Bye.....")