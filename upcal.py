# str_1=input("Enter a string:")
# def check(str_1):
#     for i in str_1:
#         if i.isupper():
#             up+=1
#         elif i.islower():
#             lp+=1
#         else:
#             pass
# print("Upper case: ",up)
# print("Lower case: ",lp)
# check(str_1)

def check(str_1):
    up=0
    lp=0
    for i in str_1:
        if i.isupper():
            up+=1
        elif i.islower():
            lp+=1
        else:
            pass
    print("Upper case: ",up)
    print("Lower case: ",lp)
str_1=input("Enter a string:")
check(str_1)
