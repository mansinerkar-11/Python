
try:
    num=int(input("Enter the Number: "))
except ValueError :
    print("Error...The entered value is floating point")
else:
    print("The number is: ",num)
finally:
    print("Bye......")
    