import unittest
import rpn

require 'coveralls'
Coveralls.wear!

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)

	def test_sub(self):
		result = rpn.calculate('4 3 -')
		self.assertEqual(1,result)
	
	def test_exp(self):
		result = rpn.calculate('3 5 ^')
		self.assertEqual(243,result)
	
	def test_toomany(self):
		with self.assertRaises(ValueError):
			result = rpn.calculate('1 2 3 +')


