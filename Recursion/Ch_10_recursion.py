##Instead of looping through a for loop, you can use recursion
##to run code inside a function and then call the function with
##different parameters at the end of the function

def printToTen(num):
  if num > 10:    ###This is called the base case
    return
  
  print(num)
  
  printToTen(num + 1)
  
printToTen(1)
  