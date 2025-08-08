# This is a list of numbers
my_list = []

# Adding some numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("My_list", my_list)

# Inserting value 15 at the second position in the list
my_list.insert(1, 15)
print("My_list", my_list)

# Expanding my_list with another list
my_list.extend([50, 60, 70])
print("My_list", my_list)

# Removing the last element from the list
my_list.pop(7)
print("My_list", my_list)

# Sorting my list in ascending order
my_list.sort()
print("My_list", my_list)

# Finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30 is", index_of_30)