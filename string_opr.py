# Write a Python program to compute following operations on String:
# a)	To display word with the longest length
# b)	To determines the frequency of occurrence of particular character in the string
# c)	To check whether given string is palindrome or not
# d)	To display index of first appearance of the substring
# e)	To count the occurrences of each word in a given string
 
str1=input("Enter String: ")
# To display word with the longest length
def longest():
    spl=str1.split()
    print(spl)
    longestword=max(spl,key=len)
    print("Longest word is: ",longestword)
    print("Length of the longest word is: ", len(longestword))

# To determines the frequency of occurrence of particular character in the string
def occ():
    char=input("Enter the alphabate to check its occurrence: ")
    counter=0
    for i in str1:
        if(char==i):
            counter+=1
    print("The frequency of occurrence of",char," in ",str1, " is: ",counter)        
        
# To check whether given string is palindrome or not
def palindrome():
    rev=str1[ : :-1]
    if(rev==str1):
        print("String is plindrome")
    else:
        print("Given string is not palindrome")

# To display index of first appearance of the substring
def substring():
    sub=input("Enter the substring to check its index: ")
    index=str1.find(sub)
    print("Index of first appearance of the substring (Note: -1 stands for string not found): ",index)
    

# 5.To count the occurrences of each word in a given string
def occount():
    counts=dict()
    word=str1.split()
    for words in word:
        if words in counts:
            counts[words]+=1
        else:
            counts[words]=1
            
        
    print("The occurrences of each word in a given string is: ",counts)

def mainf():
    print("\n 1.To display word with the longest length\n 2.To determines the frequency of occurrence of particular character in the string\n 3.To check whether given string is palindrome or not \n 4.To display index of first appearance of the substring\n 5.To count the occurrences of each word in a given string")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print("1.To display word with the longest length")
        longest()
        
    elif(ch==2):
        print("2.To determines the frequency of occurrence of particular character in the string")
        occ()
    elif(ch==3):
        print("3.To check whether given string is palindrome or not ")
        palindrome()
    elif(ch==4):
        print("4.To display index of first appearance of the substring")
        substring()
    elif(ch==5):
        print("5.To count the occurrences of each word in a given string")
        occount()
    else:
        print("Invalid choice....!")

def ask():
    asking=input("Do you want to contineu: y/n: ")
    if(asking=='y' or asking=='Y'):
        mainf()
        ask()
    else:
        exit

mainf()
ask()
