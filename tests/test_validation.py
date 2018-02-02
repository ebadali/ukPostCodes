# -*- coding: utf-8 -*-

from .context import postcodes
import unittest


class PostCodeValidationTestSuite(unittest.TestCase):
	"""This test suit tests for validation of certain inputs.
	The provided inputs in test cases covers most of the formats.

	Todo:	
		* add special uk postal code test cases 

	"""


	def shortDescription(self):
		"""preventing nose (unittest) from using the docstring"""
		return None

	def test_validate_correct(self):

		"""
		This test case demonstrates validation of all possible valid examples:
		where postcode
		-Ends with 9AA
		-contains Areas with only single-digit districts
		-contains Areas with only double-digit districts
		-contains Areas with a district 0
		
		and certain important cases
		
		-condition#1 all formats end with 9AA
		-condition#2 The letters QVX are NOT used in the first position.
		-condition#3 The letters IJZ are NOT used in the second position.
		-condition#4 The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
		-condition#5 The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
		-condition#6 The final two letters Does NOT use the letters CIKMOV, so as not to resemble digits or each other when hand-written.

		"""	

		cases = [('AA9A9AA','AA9A 9AA'), ("SW1W0NY","SW1W 0NY"), ("PO167GZ","PO16 7GZ"), 
			("GU167HF","GU16 7HF"), ("L18JQ","L1 8JQ"),("A9A9AA","A9A 9AA"),("A99AA","A9 9AA"),
			("A999AA","A99 9AA"),("AA99AA","AA9 9AA"),("AA999AA","AA99 9AA"),
			("EC1A1BB","EC1A 1BB"),("W1A0AX","W1A 0AX"),("M11AE","M1 1AE"),("B338TH", "B33 8TH"),("CR2 6XH","CR2 6XH"),("DN551PT","DN55 1PT")]		
		for unformated,formated in cases:
			self.assertTrue(postcodes.validatePostCode(formated))

	def test_validate_incorrect(self):
			
		"""This test case demonstrates invalidation of all possible invalid examples.
		Where Postcode,		
		-does not End with 9AA
		-does not contain Areas with only single-digit districts
		-does not contain Areas with only double-digit districts
		-does not contain Areas with a district 0

		and covers major cases like:
		-condition#1 all formats dose not end with 9AA
		-condition#2 The letters QVX are used in the first position.
		-condition#3 The letters IJZ are used in the second position.
		-condition#4 The only letters to appear in the third position are NOT ABCDEFGHJKPSTUW when the structure starts with A9A.
		-condition#5 The only letters to appear in the fourth position are NOT ABEHMNPRVWXY when the structure starts with AA9A.
		-condition#6 The final two letters use the letters CIKMOV, so as not to resemble digits or each other when hand-written.		
		"""

		# condition#6
		conditionSix = [('QA9A 9AAA','AA9A 9AA'),('VA9A 9AAA','AA9A 9AA'),('XA9A 9AAA','AA9A 9AA')]

		# condition#7
		conditionSeven = [('AI9A 9AAA','AA9A 9AA'),('AJ9A 9AAA','AA9A 9AA'),('AZ9A 9AAA','AA9A 9AA')]


		# condition#8
		# ILMNOQRVXYZ = LETTERS - ABCDEFGHJKPSTUW
		conditionEight = [("A9"+val+" 9AA","AA9 9AA") for val in "ILMNOQRVXYZ"]


		# condition#9
		# CDFGIJKLOQSTUZ = LETTERS - ABEHMNPRVWXY		
		conditionNine = [("AA9"+val+" 9AA","AA9A 9AA") for val in "CDFGIJKLOQSTUZ"]

		# condition#10
		# As it says on final two positions, either one of them would do 
		conditionTen = [("A9A 9"+val+""+val,"AA9A 9AA") for val in "CIKMOV"]

		cases = [("AA999 9AA","A99 9AA"),("A999 9AA","AA9 9AA"),("AAA99 9AA","AA99 9AA"),("A999 9AA","AA99 9AA"),
				('AAAA 9AA','AA9A 9AA'),('AA9A 99A','AA9A 9AA'),('AA9A AAA','AA9A 9AA'),('AA9A 9AAA','AA9A 9AA'),
				('QA9A 9AAA','AA9A 9AA'),('VA9A 9AAA','AA9A 9AA'),('XA9A 9AAA','AA9A 9AA')]

		cases = cases + conditionSix + conditionSeven +conditionEight + conditionNine + conditionTen
		
		for incorrect,correct in cases:
			self.assertFalse(postcodes.validatePostCode(incorrect))            


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(PostCodeValidationTestSuite)
	unittest.TextTestRunner(verbosity=2).run(suite)
