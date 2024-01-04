####
# Write a function that returns the intersection of two arrays. The intersection is a third array that contains all values contained within the first two arrays.
# For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] is [2, 4]. Your function should have a complexity of O(N).
# (If your programming language has a built-in way of doing this, don’t use it. The idea is to build the algorithm yourself.)


###This is not really a hash map solution

# Created a set since ``in`` works faster in a set. Sets have a built-in hash
# table which makes lookups faster than in lists.

# Not sure how to implement a hash table in python at least.

#Try creating a hash table in javascript?

def intersectionOfTwoArraysHashTable(array1, array2):
  
  intersection = []
  mySet = set(array1)

  for num in array2:
    if num in mySet:
      intersection.append(num)
  
  print(intersection)
  
  
intersectionOfTwoArraysHashTable([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])


#### For this next version, it is pretty much the same

# I realized that you need to use .get() or else you
# will get a KeyError when the key doesn't exist.

# .get([key], [default]) lets you return a default value
# if no key exists

def intersectionOfTwoArraysAttempt2(array1, array2):

  intersection2 = []
  my_hash_table = {}
  
  for num in array1:
    my_hash_table[num] = True
  
  for num2 in array2:
    if my_hash_table.get(num2, False):
      intersection2.append(num2)
  
  return intersection2
      

print(intersectionOfTwoArraysAttempt2([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]))
