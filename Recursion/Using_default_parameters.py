
#This function takes an array and doubles each number, using recursion.

                        #Uses a default parameter
def double_array(array, index=0):
  # Base case: when the index goes past the end of the array
  if (index >= len(array)):
    return

  #Body
  array[index] *= 2
  print(array)
  
  #Recursive call
  double_array(array, index + 1)  
  
double_array([1, 2, 3, 4, 5])
