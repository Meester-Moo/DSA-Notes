################################# 3 different types of doing the same thing

###                           Recursive O(N!)
def fib(n):
  if n == 0 or n == 1:
    return n
  
  return fib(n - 2) + fib(n - 1)


print(fib(6))





##                            Memoization O(N)
def fib(n, memo={}):

    if n == 0 or n == 1:
        return n

    # Check the hash table (called memo) to see whether fib(n)
    # was already computed or not:
    if not memo.get(n):

        # If n is NOT in memo, compute fib(n) with recursion
        # and then store the result in the hash table:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)

    # By now, fib(n)'s result is certainly in memo. (Perhaps
    # it was there before, or perhaps we just stored it there
    # in the previous line of code. But it's certainly there now.)
    # So let's return it:
    return memo[n]
  
print(fib(6))




###                           Bottom-up approach O(N)
def fib(n):

    if n == 0:
        return 0

    # a and b start with the first two numbers in the series, respectively:
    a = 0
    b = 1

    # Loop from 1 until n:
    for i in range(1, n):

        # a and b each move up to the next numbers in the series.
        # Namely, b becomes the sum of b + a, and a becomes what b used to be.
        # We utilize a temporary variable to make these changes:
        temp = a
        a = b
        b = temp + a

    return b

print(fib(6))



###Dynamic Programming just means reducing duplicate recursive calls.

###Can do this either with Memoization or with an approach that doesn't
###even involve any recursion (Bottom up approach) 