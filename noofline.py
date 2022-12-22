# #Write a Python program to read a text file and print number of lines,
# #words and charecters
# fp=open("second.txt","r")
# print(fp.read())
# fp.seek(0)
# nlines=0
# nwords=0
# ncharacter=0
# for line in fp:
#     line=line.strip("\n")
#     nlines+=1
#     words=line.split()
#     nwords+=len(words)
#     ncharacter+=len(line)
# fp.close()
# print("lines:",nlines,"word:",nwords,"character:",ncharacter)
# 
# 
# 
# 
# x="manSi"
# y="HELLO"
# print(str.upper(x))
# print(str.upper(y))

import keyword
str1="else"
print(keyword.iskeyword(str1))

