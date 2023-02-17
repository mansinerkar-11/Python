#Write python program using function to find greatest of three numbers by passing numbers as argument
# function to find the greater number among 3
def my_function(num1,num2,num3):
    if num1>num2 and num1>num3:
        #if yesss then
        print("greater number is num1: ",num1);
    # if the above condition is false then it can be
    elif num2>num1 and num2>num3:
        # if yesssss then 
        print("greater number is num2: ",num2);
        # if the above condition is false then we know num 3 will greater 
    else:
        print("greater number is num3: ",num3)
# To acceot the numbers from the user
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

my_function(num1,num2,num3)

