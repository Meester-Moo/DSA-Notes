###This is an example of "Stack Overflow"

#It can happen when a recursive function is called so many times
#that it fills up the memory, such as in an infinite recursive loop


def stackOverflow(number):

  ##no base statement (recursive function infinitely repeats itself)
  
  num = number
  
  print(f'This function has been called {num} times')
  
  stackOverflow(num + 1)
  
  

stackOverflow(1)