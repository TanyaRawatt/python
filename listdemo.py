# #list can store multiple data,data can be different types int str
# #list can store the duplicate data
# #list is an ordered data dataset --sorting ascending descending

# #create list and store the your friends name

# friendlist=["ivan","anshu","anjali","vani"]

# #print the list of friend names
# # print(friendlist)

# #add the age of your friends into list 
# #append will add the data into end of the list
# friendlist.append(36)
# friendlist.append(26)
# friendlist.append(36)
# friendlist.append(25)
# # print(friendlist)

# #add the data into list using index no

# friendlist.insert(0 ,"ayush")
# friendlist.insert(3,"tanya")
# print(friendlist)

# #to access the data using index
# # print(friendlist[3])

# # for name in friendlist:
# #     print(name)
    
    
# #to delete the data from list
# #remove will delete the data using value
# # friendlist.remove("tanya")
# # print(friendlist)

# #pop will delete the data using index 
# #by default pop will delete last index value
# friendlist.pop(3)
# print(friendlist)

# friendlist.pop(0)
# print(friendlist)

#add the 5 fvt city name in list
#add my fav city kasol in first index
#remove the last city in list
#sorting the list data
#print the list data

city=["ghaziabad","noida","kasol","roorkee","amristsar"]
city.insert(0,"dehradun")
city.pop()
city.sort()
print(city)
