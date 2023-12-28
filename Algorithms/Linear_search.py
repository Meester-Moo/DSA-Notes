def greatestNumber(array):
  max = array[0]
  for num in array:
    if num > max:
      max = num
  return max
  
print(greatestNumber([2, 1, 5, 3, 4]))
#returns 5
