l1=()
l1size=int(input("Enter size of list: "))
for i in range(0,l1size):
    value=input("Enter vowels: ")
    if((value=='a' or value=='A')or (value=='e' or value=='E')or (value=='i' or value=='I') or (value=='o' or value=='O') or (value=='u' or value=='U')):
        l1=l1+(value,)
print(l1)
print(type(l1))

