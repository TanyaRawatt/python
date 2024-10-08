#create read write delete json
mydata=open("myfile.json","w")

mydata.write("My name is Tanya Rawat and my roll number is 43\n")

mydata.write(input("enter  your new roll number:"))

mydata=open("myfile.json","r")
print(mydata.read())

mydata=open("myfile.json","r")
myvalue=mydata.read()
if "Tanya" in myvalue:
    print("yes")
else:
    print("no")

mydata.close()

import os
os.remove("myfile.json")