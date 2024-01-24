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
  ### This returns the second element plus
  ### all of the other elements
  
  ### This line returns
  ### a recursive stack of calls like this?:
    ### call 1: array[0] + array[1]
    ###   call 2: array[0] + array[2]
    ###     call 3: array[0] + array[3]
    ###       call 4: array[0] + array[4]
    ###         call 5: array[0] + array[5]
    
  ###
  

print(arraySum([1, 2, 3, 4, 5]))