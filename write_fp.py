# 39. Write a python program to:- 
# a. Read file contents(all)
# b. Read characters from 26-50
# c. Write 2 lines in a file
# fp=open("second.txt","w")
# # 
# fp.write("This is first line\nThis is second line\nThis is third line\nThis is fourth line")
# # print(fp.read())
# fp.close()

fp=open("second.txt","r")
print(fp.read()[26:51])
fp.seek(0)
fp.close()