from app import prime

import unittest

class primeNumberTestCase(unittest.TestCase):
	def test_if_number_passed_is_prime(self):
		self.assertEqual(prime.prime_numbers(5), [2,3])
	def tes_if_output_is_list(self):
		self.assertIsInstance(prime.prime_numbers(14), list)	
	def test_if_number_is_one(self):
		self.assertEqual(prime.prime_numbers(1),"a prime number is greater than one")
	def test_if_number_is_zero(self):
		self.assertEqual(prime.prime_numbers(0),"a prime number is greater than one")
	def test_if_number_is_two(self):
		self.assertEqual(prime.prime_numbers(2),[2])
	def test_if_number_is_three_or_less(self):
		self.assertEqual(prime.prime_numbers(3),[2,3])			
	def test_less_than_zero(self):
		self.assertEqual(prime.prime_numbers(-1),"a prime number is greater than one")
	def test_number_type_not_string(self):
		self.assertEqual(prime.prime_numbers("string"),"Only integers allowed")
	def test_number_type_not_list(self):
		self.assertEqual(prime.prime_numbers([]),"Only integers allowed")
	def test_number_type_not_dictionary(self):
		self.assertEqual(prime.prime_numbers({}),"Only integers allowed")
		
	
