#Q6. Write a program to calculate surface volume and area of a cylinder.
r=int(input("Enter the radius of cylinder: "))
h=int(input("enter the height of cylinder: "))
volume=(22/7)*r*r*h
area=2*(22/7)*r*h+2*(22/7)*r*r
print("Volume of cylinder is:",volume)
print("Area of cylinder is:",area)