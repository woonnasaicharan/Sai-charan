## Create a list of numbers (Eg. 34, 35, 84, 23, 19)
## sort the list in ascending order 
## remove number 23 from the list
## print the list

numbers = [34, 35, 84, 23, 19]
print("list",numbers)

numbers.sort()
print("Sorted list:", numbers)

numbers.remove(23)               
print("List after removing 23:", numbers)

