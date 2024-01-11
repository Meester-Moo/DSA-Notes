def reverseString(mystring):
  
  #Base case
  if len(mystring) == 1:
    return mystring
  else:
    return reverseString(mystring[1:]) + mystring[0]
  
    

print(reverseString('hello'))
###Output: olleh