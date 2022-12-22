# Name: Naik Anushka Balasaheb      Class: TYCM1     Roll.No: 37
# Practical.No: 03
# Title: Write simple python program using operators: Arithemitic, Logical, Bitwise.

# Exercise Question-1: Write a program to convert U.S. dollars to Indian rupees.
# usd = float(input("Enter currency in USD: "))
# inr = usd * 73
# print("The currency in INR is",round(inr,2))
# Output:-
# Enter currency in USD: 5
# The currency in INR is 365.0
# Enter currency in USD: 1234
# The currency in INR is 90082.0

# Exercise Question-2: Write a program to convert bits to megabytes, gigabytes and terabytes.
# bi = int(input("Enter bit: "))
# mg = bi * (1.25 * (10 ** -7))
# gg = bi * (1.25 * (10 ** -10))
# tg = bi * (1.25 * (10 ** -13))
# print(bi," bit in megabytes",mg)
# print(bi," bit in gigabytes",gg)
# print(bi," bit in terabytes",tg)
# Output:-
# Enter bit: 1
# 1  bit in megabytes 1.25e-07
# 1  bit in gigabytes 1.25e-10
# 1  bit in terabytes 1.25e-13
# Enter bit: 2
# 2  bit in megabytes 2.5e-07
# 2  bit in gigabytes 2.5e-10
# 2  bit in terabytes 2.5e-13
# Exercise Question-3: Write a program to find square root of a number.
# no = int(input("Enter a number: "))
# no_st = no ** 0.5
# print("The square root of %0.3f is %0.3f"%(no ,no_st))
# Output:-
# Enter a number: 4
# The square root of 4.000 is 2.000
# Enter a number: 49
# The square root of 49.000 is 7.000


# Exercise Question-4: Write a program to find the area of rectangle.
# rl = float(input("Enter the length of rectangle: "))
# rb = float(input("Enter the breadth of rectangle: "))
# print("Area of rectangle:",rl*rb,"sq.cm")
# Output:-
# Enter the length of rectangle: 4
# Enter the breadth of rectangle: 3
# Area of rectangle: 12.0 sq.cm

# Exercise Question-5: Write a program to calculate area and perimeter of the square.
# side = float(input("Enter the side of the square: "))
# print("Area of Square:",side*side,"sq.cm")
# print("Perimeter of Square:",4*side,"cm")
# Output:-
# Enter the side of the square: 7
# Area of Square: 49.0 sq.cm
# Perimeter of Square: 28.0 cm

# Exercise Question-6: Write a program to swap the value of two numbers.
# no1 = int(input("Enter Number-1: "))
# no2 = int(input("Enter Number-2: "))
# no3 = no1
# no1 = no2
# no2 = no3
# print("Value of Number-1 after swapping:",no1)
# print("Value of Number-2 after swapping:",no2)
# Output:-
# Enter Number-1: 23
# Enter Number-2: 10
# Value of Number-1 after swapping: 10
# Value of Number-2 after swapping: 23

# Second method of swapping
# no1 = int(input("Enter Number-1: "))
# no2 = int(input("Enter Number-2: "))
# 
# no1,no2 = no2,no1
# print("Value of Number-1 after swapping:",no1)
# print("Value of Number-2 after swapping:",no2)
# Output:-
# Enter Number-1: 2
# Enter Number-2: 3
# Value of Number-1 after swapping: 3
# Value of Number-2 after swapping: 2

# Name: Naik Anushka Balasaheb      Class: TYCM1     Roll.No: 37
# Practical.No: 03
# Title: Write simple python program using operators: Arithemitic, Logical, Bitwise.

# Bitwise Operators
# a = 10
# b = 4
# print("If a = 10(1010) and b = 4(0100):-")
# print("Bitwise AND:",a&b)
# print("Bitwise OR:",a|b)
# print("Bitwise NOT for a:",~a)
# print("Bitwise NOT for b:",~b)
# print("Bitwise XOR:",a^b)
# print("Bitwise right shift:",a>>2)
# print("Bitwise left shift:",a<<2)

# Logical Operators
# >>> (10>8) and (8<9)
# True
# >>> (10<8) and (8>9)
# False
# >>> (2 == 3) or (5 > 4)
# True
# >>> (2 != 2) or (5 < 4)
# False
# >>> not(8>2)
# False
# >>> not(2>10)
# True



