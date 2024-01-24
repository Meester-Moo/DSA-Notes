# Write a function that accepts a string that contains all the letters of the alphabet
# except one and returns the missing letter. For example, the string, "the quick brown
# box jumps over a lazy dog" contains all the letters of the alphabet except the letter,
# "f". The function should have a time complexity of O(N).

def myFunction(my_string):
  
  dictionary = {}
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  
  for character in my_string:
    dictionary[character] = True
  
  for character in alphabet:
    if not dictionary.get(character, False):
      return character
    
  
print(myFunction('thequickbrownboxjumpsoveralazydog'))


#So I guess what I tried was creating a hash table (dictionary) with the alphabet
#and looping through the string.

#What I should have done was create a dictionary with my string and loop
#through the alphabet.