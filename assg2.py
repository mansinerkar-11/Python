#1:To display word with the longest length
str1=input("enter string:")
def lngword():
	spl=str1.split()
	print(spl)
	longword=max(spl,key=len)
	print("Long word is :",longword)
	print("Length of longest word is:",len(longword))
#2:To check whether given string is palindrome or not
def palindr():
	str2=str1[::-1]
	print(str2)
	if str2==str1:
		print("string is palindrome")
	else:
		print("String is not palindrome")

#3:To determines the frequency of occurrence of particular character in the string
def countch():
	a=input("enter the character:")
	count=0
	for i in str1:
		if i==a:
			count+=1
	print(count)

#4:To count the occurrences of each word in a given string
def wordcount():
	word=0
	dict1={}
	spl=str1.split()
	for k in range(len(spl)):
		v=spl[k]
		for j in range(len(spl)):
			if spl[j]==v:
				word+=1
		print(word)
		dict1[v]=word
		word=0
	print(dict1)
#5:To display index of first appearance of the substring
def substringind():
	substr=input("Enter substring :")
	b=str1.find(substr)
	print(b)
def mainf():
	print("\n--------------------------------\n")
	print('''1.find Longest word\n2.Frequency of character\n3.Check palindrome\n4.Display index of substring\n5.word count\n''')
	print("\n--------------------------------\n")
	ch=int(input("Enter given choice:"))
	if ch==1:
		lngword()
	elif ch==2:
		countch()
	elif ch==3:
		palindr()
	elif ch==4:
		substringind()
	elif ch==5:
		wordcount()
	else:
		print("wrong choice")
def ask():
    opt=input("Do u want to continue Y/N :")
    if(opt=='y' or opt=='Y'):
            mainf()
            ask()
    else:
        exit

mainf()
ask()

	







