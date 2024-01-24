def max(array)

  # Base case - if the array has only one element, it is
  # by definition the greatest number:

  return array[0] if array.length == 1

  # Compare the first element with the greatest element
  # from the remainder of the array. If the first element
  # is greater, return it as the greatest number:
  if array[0] > max(array[1, array.length - 1])
    return array[0]
  # Otherwise, return the greatest number from the remainder of the array:
  else
    return max(array[1, array.length - 1])
  end
end



####Improved version:


def max(array)
  return array[0] if array.length == 1
  max_of_remainder = max(array[1, array.length - 1])
  if array[0] > max_of_remainder
    return array[0]
  else
    return max_of_remainder
  end
end
