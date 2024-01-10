#################### Iterative loop
def factorial(n)
  product = 1
  (1..n).each do |num|
    product *= num
  end
    return product
end

#################### Top down approach
def factorial(number)
  if number == 1
    return 1
  else
    return number * factorial(number - 1)
  end
end

#################### Bottom up approach
def factorial(n, i=1, product=1)
  return product if i > n
  return factorial(n, i + 1, product * i)
end
    