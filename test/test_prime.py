from app import prime

import unittest

class primeNumberTestCase(unittest.TestCase):
	def test_if_number_passed_is_prime(self):
		self.assertEqual(prime.prime_no(5), [2,3])
	def tes_if_output_is_list(self):
		self.assertIsInstance(prime.prime_no(14), list)	
	def test_if_number_is_one(self):
		self.assertEqual(prime.prime_no(1),"a prime number is greater than 1")
	def test_if_number_is_zero(self):
		self.assertEqual(prime.prime_no(0),"a prime number is greater than 0")
	def test_if_number_is_two(self):
		self.assertEqual(prime.prime_no(2),[2])
	def test_if_number_is_three_or_less(self):
		self.assertEqual(prime.prime_no(3),[2,3])			
	def test_less_than_zero(self):
		self.assertEqual(prime.prime_no(-1),"No negative prime numbers")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no("string"),"Only integers allowed")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no([]),"Only integers allowed")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_no({}),"Only integers allowed")
		
	
