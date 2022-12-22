#Write a python program to read contents of first.txt file and write in second.txt

with open('first.txt','r') as firstfile:
    with open('second.txt','a') as secondfile:
        for line in firstfile:
            secondfile.write(line)
print("Contends copied successfully")
fp=open("second.txt","r")
print(fp.read())
fp.close()