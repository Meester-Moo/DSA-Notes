
###This is not really a hash map solution

# def intersectionOfTwoArrays(array1, array2):
#   print("hello world")

#   intersection = []
  
#   for num in array1:
#     if num in array2:
#       intersection.append(num)
  
#   print(intersection)
  
  

# intersectionOfTwoArrays([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])



def intersectionOfTwoArraysHashTable(array1, array2):
  
  intersection = []
  mySet = set(array1)

  for num in array2:
    if num in mySet:
      intersection.append(num)
  
  print(intersection)
  
  
intersectionOfTwoArraysHashTable([1, 2, 3, 4, 5], [0, 2, 4, 6, 8])