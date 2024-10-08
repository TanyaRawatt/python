#list in python
#list store multiple data
myList=["tanya","ivan","deepanshu","tanya"]
#tuple store multiple data
myTuple=("tanya","ivan","deepanshu","tanya")
#set store multiple data
mySet={"tanya","ivan","deepanshu","tanya"}
#dictionary store multiple data in key value pair
myDict={"name":"tanya","name":"tanya","email":"rwttanya2506@gmail.com"}

#to check the data type of all the data set
print("list:",type(myList),"tuple:",type(myTuple))
print("set:",type(mySet),"dict:",type(myDict))

#how to identify list,set,tuple,dictionary

#tuple-->( )== can store duplicate item
#set-->{ }==  no duplicate item  
#list-->[ ]== list can have duplicate item
#dictionary--> { : }== no duplicate item

#access data from data set
print("list:",myList[0])
print("tuple:",myTuple[0])
print("dict:",myDict["name"])

#access complete data from data  set
for data in myList:
    print("list",data)
for item in mySet:
    print("set",item)
for value in myTuple:
    print("tuple",value)
for x in myDict.values():
    print("dict",x) 

# to update the data in all data set

myList[0]="rawat"
print(myList)
# list in changeable

# myTuple[0]="rawat"
# print(myTuple)
# #tuple is not changeable

# mySet[0]="rawat"
# print(mySet)
# #set is not changeable

myDict["name"]="rawat"
print(myDict)
#dict is changeable 
#[0]==is not the index value instead is a keyword

#add new value in data set
myList.append("dipsy")
mySet.add("dipsy")
myDict.update({"name":"dipsy"})
#it can store only 1 element at a time
print("list",myList,"tuple",myTuple,"dict",myDict,"set",mySet)

# to remove the data from data set
myDict.pop("name")
myList.pop(0)
mySet.remove("tanya")
print("list",myList,"tuple",myTuple,"dict",myDict,"set",mySet)


#you can not update or change anything in tuple
#tuple only comes with 2 functions

#convert tuple to list
convertlist=list(myTuple)
print(type(convertlist))

convertlist.append("stdbv")
convertlist.pop(2)
print(convertlist)


