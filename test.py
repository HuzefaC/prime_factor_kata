import unittest
from prime_factor import get_prime_factors

class TestPrimeFactor(unittest.TestCase):
  def test_prime_factor_of_1(self):
    self.assertListEqual(get_prime_factors(1), [])


if __name__=='__main__':
  unittest.main()