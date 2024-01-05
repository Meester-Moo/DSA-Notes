#this is how you might create a stack in python

my_list = []

my_list.append(3)

print(my_list) # stack = [3]

my_list.append(7) # stack = [3, 7]
my_list.append(5) # stack = [3, 7, 5]
my_list.append(2) # stack = [3, 7, 5, 2]

print(my_list) # stack = [3, 7, 5, 2]

my_list.pop() #pop without storing the popped item
#stack = [3, 7, 5]

my_element = my_list.pop() #store popped item in a variable
#stack = [3, 7]

print(my_list)

#add 5 and 2 back to the stack
my_list.append(5)
my_list.append(2)

#peek, means to access a value without removing it from the stack
print(my_list[-1])

###### It turns out that in python to peek, you just access the index of the list.

###### You can peek at the last element (the top of the stack) by doing my_list[-1]

###### Remember that the right most element is the top of the stack, so it's like
###### flipping the array counterclockwise 90 degrees.