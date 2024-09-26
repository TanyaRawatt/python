userage=int(input("enter your age="))
usergender=input("enter your gender=")


#using logical operators

if usergender=="female" and userage>=18:
    print("you are eligible for govt job")
elif usergender=="male" and userage>=18:
    print("you are eligible for private job")
else:
    print("not eligible")



#using if else statements

# if userage>=18:
#     if usergender=="male":
#         print("you can apply for prvt job")
#     elif usergender=="female":
#         print("you can apply for govt job")
#     else:
#         print("sorry there is no opening")
# else:
#     print("you are underage")