#conditional statement will check the condition
# to check the condition we use if else
#wap to check user eligible for voting

userage=int(input("enter your age="))

#note the default input function return type is string
#for vote userage must be greater than 18


if userage>=18:
    print("you are eligible for voting")
else:
    print("you are not eligible for voting")