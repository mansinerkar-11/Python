fp=open("myfile.txt", "r+")
fp.write("Hi everyone, how are you?")
print(fp.tell()) 
fp.seek(0,0)
print(fp.tell())
fp.read(15)
fp.seek(0,1)
print(fp.tell())
fp.seek(0,2)
print(fp.tell())
fp.close()
