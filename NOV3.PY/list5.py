#Assignment 5
## Create a list of five city names
## insert a new city at the third position
## append a new city at the end
## reverse the list
## remove the exact middle element using del
## print the list


citys = ["vizag","hydarabad","vijaynagram","mumbai","delhi"]
citys.insert(2,"bangaluru")
print("citys new",citys)
citys.append("chenni")
print("ssscity",citys)
citys.reverse()
middle_index = len(citys) // 2
del citys[middle_index]
print("Final list of cities:", citys)



