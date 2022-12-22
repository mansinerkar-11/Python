#ASSIGNMENT2
"""Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the substring
e) To count the occurrences of each word in a given string

Name: Atharva M Sangle
Roll No. 56
Class - COMP SE_B  

"""
# check palindrome
def palindrome():
	str2 = str1[::-1]
	if str1 == str2:
		print(str1,"is a palindrome")
	else:
		print("Not a palindrome")
#find longest word
def long():
	
	longword = max(spl,key = len)
	print("Longest word = ", longword)
#find substring
def sub():
	substr= input("Enter substring to be searched:")
	print(str1.find(substr))

#to check frequency of a char
def freq():
	count =0
	char = input("Enter character to check frequency")
	for i in str1:
		if i == char:
			count+=1
	print("frequency of ",char ,"is",count)	
#occurence of each word
def occu():
	count1 = 0
	dict1= {}
	for word in range(0,len(spl)):
		for new in range(0,len(spl)):
			if spl[word]== spl[new]:
				count1+=1
		dict1[spl[word]]= count1
		count1 = 0
	print(dict1)


while True:

	str1 = input("Enter string : ")
	spl = str1.split()
 	#Display Choice 
	print("\t\t MENU \n")
	print(" Enter 1 to check palindrome\n Enter 2 to find longest word\n Enter 3 to find first occurence of substring\n Enter 4 to find frequency of char\n Enter 5 to display occurences of each word \n Enter 6 to exit")
	a =int(input(" Enter choice:"))


	if a == 1:
		palindrome()
	elif a ==2:
		long()
	elif a ==3:
		sub()
	elif a ==4:
		freq()
	elif a ==5:
		occu()
	elif a ==6:
		print(" Exiting")
		break
