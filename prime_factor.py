def get_prime_factors(number):
  prime_factors = []
  if number > 1:
    if number % 2 == 0:
      prime_factors.append(2)
      number = number // 2
    if number > 1:
      prime_factors.append(number)
  return prime_factors