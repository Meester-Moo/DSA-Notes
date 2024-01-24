def greatestNumber(array):
  for i in array:
    is_greatest = True  # Use snake_case for variable names
    for j in array:
      if j > i:
        is_greatest = False
    if is_greatest:
      return i
    

