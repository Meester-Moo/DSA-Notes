#Write a function that accepts an array of strings and returns the first duplicate value it finds.
# For example, if the array is ["a", "b", "c", "d", "c", "e", "f"], the function should return
# "c", since it’s duplicated within the array. (You can assume that there’s one pair of duplicates
# within the array.) Make sure the function has an efficiency of O(N).

def myFunction(my_list):
  
  my_dict = {}
  
  for str in my_list:
    if my_dict.get(str, False):
      return str
    
    my_dict[str] = True
    

print(myFunction(['a', 'b', 'c', 'd', 'c', 'e', 'f']))

#For this one, I got stuck on the fact that you have to check if
#the item is already in the dictionary BEFORE you add a new one.

#Because otherwise each item will already be in there before
#you check and therefore the first item will always return.