def get_prime_factors(number):
  prime_factors = []
  divisor = 2
  while number > 1:
    while number % divisor == 0:
      prime_factors.append(divisor)
      number = number // divisor
    divisor += 1
  return prime_factors