#error in progress
#error 1
#print(x)

#solution
try:
    print(x)
except NameError:
    print("x is not defined")


#error 2
# y=1/0

try:
    y=1/0
except ZeroDivisionError:
    print("division by zero not possible")
    
#error 3
name="tanya"
# no=int(name)

try:
    no=int(name)
except ValueError:
    print("string cant convert into integer")
    
#error 4
friends=["ivan","anshu","vani"]
# friends[4]

try:
    friends[4]
except IndexError:
    print("index 4 is not present")

#error 5
amount=500
email="p@gmail.com"
# total=amount+email

try:
    total=amount+email
except TypeError:
    print("string cant concatenate with integer")

 