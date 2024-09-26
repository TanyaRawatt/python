#function can perform any task
#it can be reuse, function will return the result 


#create function to print the name
def printname():
    print("my name is tanya")

#call function to print the name
printname()

#create function to concatenate fname and lname from user
fname=input("enter your first name=")
lname=input("enter your last name=")

def printfullname(firstname,lastname):
    print(firstname+lastname)

printfullname(fname,lname)