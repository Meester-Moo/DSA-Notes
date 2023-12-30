#################### Linear Search in Ruby (Ordered Array)


def​linear_search​(array, search_value)
	
	  ​# We iterate through every element in the array:​
	  array.​each_with_index​do|element, index|
	
	    ​# If we find the value we're looking for, we return its index:​
	    ​ifelement == search_value
	      ​returnindex
	
	    ​# If we reach an element that is greater than the value​
	    ​# we're looking for, we can exit the loop early:​
	    ​elsifelement > search_value
	      ​break​
	    ​end​
	  ​end​
	
	  ​# We return nil if we do not find the value within the array:​
	  ​return​nil​
	
	​end​


## This example was used to show that a linear search is usually more efficient (one exception = element is at the end)
## on an ordered array than a classic, unordered array because it stops
## sooner if the next value is greater than or equal to the search_value



