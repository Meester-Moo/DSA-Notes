# import unittest

def selectionSort(array):
  for i in range(len(array) - 1):
    lowestNumIndex = i
    for j in range(i + 1, len(array)):
      if array[j] < array[lowestNumIndex]:
        lowestNumIndex = j
  
    if (lowestNumIndex != i):
      temp = array[i]
      array[i] = array[lowestNumIndex]
      array[lowestNumIndex] = temp
  
  return array
    
print(selectionSort([2,7,3,1,5,4])) #manual unit test

# class TestSelectionSort(unittest.TestCase):
#   def test_selectionSort(self):
#     self.assertEqual(selectionSort([2,7,3,1,5,4]), [1,2,3,4,5,7])
#     self.assertEqual(selectionSort([10, -1, 2, 5, 0]), [-1, 0, 2, 5, 10])
#     self.assertEqual(selectionSort([]), [])
#     self.assertEqual(selectionSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])  # already sorted
#     self.assertEqual(selectionSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])  # reverse sorted
#     self.assertEqual(selectionSort([2, 2, 2, 1, 1]), [1, 1, 2, 2, 2])  # duplicates
#     self.assertEqual(selectionSort([1]), [1])  # single element
#     self.assertEqual(selectionSort([-2, -5, -1]), [-5, -2, -1])  # negative numbers

# if __name__ == '__main__':
#   unittest.main()


## I tried seeing what unit tests look like in Python with GitHub copilot^^