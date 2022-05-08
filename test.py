import unittest
from prime_factor import get_prime_factors

class TestPrimeFactor(unittest.TestCase):
  def test_prime_factor_of_1(self):
    self.assertListEqual(get_prime_factors(1), [])

  def test_prime_factor_of_2(self):
    self.assertListEqual(get_prime_factors(2), [2])

  def test_prime_factor_of_3(self):
    self.assertListEqual(get_prime_factors(3), [3])

  def test_prime_factor_of_4(self):
    self.assertListEqual(get_prime_factors(4), [2, 2])

  def test_prime_factor_of_5(self):
    self.assertListEqual(get_prime_factors(5), [5])

  def test_prime_factor_of_6(self):
    self.assertListEqual(get_prime_factors(6), [2, 3])

  def test_prime_factor_of_7(self):
    self.assertListEqual(get_prime_factors(7), [7])

  def test_prime_factor_of_8(self):
    self.assertListEqual(get_prime_factors(8), [2, 2, 2])   


if __name__=='__main__':
  unittest.main()