#create read write delete excel
mydata=open("excel.xlxs","w")

mydata.write("my name is Tanya Rawat and my roll number is 43\n")

mydata.write(input("enter  your new roll number:"))

mydata=open("excel.xlxs","r")
print(mydata.read())

mydata=open("excel.xlxs","r")
myvalue=mydata.read()
if "Tanya" in myvalue:
    print("yes")
else:
    print("no")

mydata.close()

import os
os.remove("excel.xlxs")
    

