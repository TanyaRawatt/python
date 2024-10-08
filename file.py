#create file for saving my laptop password
#open function will create the file
#when file is not exists
myPassword=open("personal.txt","w")

#write my laptop password in file
myPassword.write(" my android password=tannu")


#overwrite the new password using user input 
myPassword.write(input("enter your new password"))

#read the password from file

myPassword=open("personal.txt","r")
print(myPassword.read())  
# readmode

#read the password from file
myPassword=open("personal.txt","r")
mydata=myPassword.read()
if "android" in mydata:
    print("yes")
else:
    print("no")
    
#close the file
myPassword.close()

#delete the file
import os
os.remove("personal.txt")

