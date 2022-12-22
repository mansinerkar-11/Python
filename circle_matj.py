import math as m
#circumference = 2*pi*r
#area=pi*r*r
r=int(input("Enter radius of circle: "))
def area(r):
    ar_cal= m.pi*r*r
    print("Area of circle is: ",ar_cal)
def circum(r):
    cir_cal= 2*m.pi*r
    print("Cicrcumference of circle is: ",cir_cal)
area(r)
circum(r)