########  Make a top-down approach recursive function
#         that takes an array an returns the sum of the
#         elements in the array


def arraySum(array):
  
  ### Base case
  ### We start off with dealing with an array of length 1.
  if len(array) == 1:
    return array[0]
  
  ### Then we figure out the subproblem is the adding of
  ### each element in the array
  else:
    return array[0] + arraySum(array[1:])
  ### This returns the first element plus
  ### a recursive stack of calls like this:
    ### array[0] + array[1]
    ### array[0] + array[2]
    ### array[0] + array[3]
    ### array[0] + array[4]
    ### array[0] + array[5]
    
  ### in 
  

print(arraySum([1, 2, 3, 4, 5]))