from app import prime

import unittest

class primeNumberTestCase(unittest.TestCase):
	def test_if_number_passed_is_prime(self):
		self.assertEqual(prime.prime_no(7), [2,3,5])
	def test_if_number_less_than_2(self):
		self.assertEqual(prime.prime_no(1),"prime number is greater than one")
	def test_if_number_less_than_2(self):
		self.assertEqual(prime.prime_no(0),"prime number is greater than one")	
	def test_less_than_zero(self):
		self.assertEqual(prime.prime_no(-1),"No negative prime numbers")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no("string"),"Only integers allowed")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no([]),"Only integers allowed")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no({}),"Only integers allowed")
	
