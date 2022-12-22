# Write a Python script to sort (ascending and descending) a dictionary by value.
d={}
keyd=()
size=int(input("Enter the size of dictionary: "))
for i in range(0,size):
    k=input("Enter key:")
    keyd+=(k,)
    val=input("Enter value: ")
    d[i]=val
d[i].fromkey(keyd)
print(d)