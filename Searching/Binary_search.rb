#################### Binary Search in Ruby (Ordered Array)
## much faster than linear search
## binary search can only be done on an ordered array

def​binary_search​(array, search_value)
  	
  ​# First, we establish the lower and upper bounds of where the value​
  ​# we're searching for can be. To start, the lower bound is the first​
  ​# value in the array, while the upper bound is the last value:​

  lower_bound = 0
  upper_bound = array.​length- 1

  ​# We begin a loop in which we keep inspecting the middlemost value​
  ​# between the upper and lower bounds:​

  ​whilelower_bound <= upper_bound ​do​

    ​# We find the midpoint between the upper and lower bounds:​
    ​# (We don't have to worry about the result being a non-integer​
    ​# since in Ruby, the result of division of integers will always​
    ​# be rounded down to the nearest integer.)​

    midpoint = (upper_bound + lower_bound) / 2

    ​# We inspect the value at the midpoint:​

    value_at_midpoint = array[midpoint]
    ​# If the value at the midpoint is the one we're looking for, we're done.​
    ​# If not, we change the lower or upper bound based on whether we need​
    ​# to guess higher or lower:​

    ​ifsearch_value == value_at_midpoint
      ​returnmidpoint
    ​elsifsearch_value < value_at_midpoint
      upper_bound = midpoint - 1
    ​elsifsearch_value > value_at_midpoint
      lower_bound = midpoint + 1
    ​end​
  ​end​

  ​# If we've narrowed the bounds until they've reached each other, that​
  ​# means that the value we're searching for is not contained within​
  ​# this array:​

  ​return​nil​
​end​