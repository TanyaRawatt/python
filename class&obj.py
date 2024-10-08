#oops in python
#object oriented programming structure

#class-> it is a container which collect variables,function
#example->tanya  rawat
#tanya.fullname="tanyarawat"
#tanya.age=18
#tanya.sleeping()
#tanya.eating()
#tanya.watching()

#class syntax
class ClassName:
    print("this is my class")

class Tanya:
    age=18
    fullName="tanya rawat"
    email="rwttanya2506@gmail.com"
    def pocketMoney(this,amount):
        print("my pocket money is ",amount)
    
    def monthly(this,daysalary):
        print("my 1 day income is ",daysalary)
        print("my monthly income is ",daysalary*30)

#create class object
tanya:Tanya=Tanya()
#object:class=class()

print("my name is ",tanya.fullName)
print("my age is ",tanya.age)
print("my email is ",tanya.email)
tanya.pocketMoney(1000)
tanya.monthly(int(input("enter your one day salary:")))