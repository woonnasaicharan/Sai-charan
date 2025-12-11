#Assignment 2
#create a list of five colors - red, yellow, green, blue, black
# convert them into tuple and print it
# convert it back to list and add "white"
# convlert it back to tuple and print



colors = ["red", "yellow", "green", "blue", "black"]
colors_tuples = tuple(colors)
print("Tuple:", colors_tuples)
colour_list = list(colors_tuples)
print("lits",colour_list)
colour_list.append("white")
print("new list",colour_list)
final_tuples=tuple(colour_list)
print("final_tuplesss",final_tuples)



