def sum_divisors(n):
  sum = 0
  # Return the sum of all divisors of n, not including n
  m = 1
  while m < n:
 
    if n % m == 0:
      sum = sum + m

    m += 1

   
  return sum
# returns the sum of all the divisors of a number, without including it
