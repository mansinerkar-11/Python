#Write a Python program to perform following operations on set:
#intersection of sets, union of sets, set difference, symmetric difference,clear a set.
s1=set()
s2=set()
size1=int(input("Enter The Size of Set 1: "))
for i in range(0,size1):
    var=input("Insert Element:")
    s1.add(var)
size2=int(input("Enter The Size of Set 2: "))
for i in range(0,size2):
    var=input("Insert Element:")
    s2.add(var)
print("Set 1:",s1)
print("Set 2:",s2)
print("______________Intersection of sets_____________")
print("Set after intersection: ",s1&s2)
print("______________Intersection of sets_____________")
print("Set after intersection: ",s1&s2)
print("______________union of sets_____________")
print("Set after union: ",s1.union(s2))
print("______________Difference of sets_____________")
print("Set after Difference: ",s1-s2)
print("______________symmetric difference of sets_____________")
print("Set after symmetric difference: ",(s1-s2)^(s2-s1))
print("______________clear_____________")
print("Set after clear: ",set.clear(s1))
print(s1)
print("Set after clear: ",set.clear(s2))
print(s2)

