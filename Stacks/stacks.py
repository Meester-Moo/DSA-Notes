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