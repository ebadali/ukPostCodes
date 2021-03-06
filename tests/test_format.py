# -*- coding: utf-8 -*-

from .context import postcodes
import unittest


class PostCodeFormatTestSuite(unittest.TestCase):
	"""This test suit tests for Formatting of outputs on certain inputs.
	The provided inputs in the test cases covers most of the formats.

	Todo:	
		* add special uk postal code test cases 
		
	"""

	def shortDescription(self):
		"""preventing nose (unittest) from using the docstring"""
		return None


	def test_format_correct(self):
		
		"""
		This test case demonstrates formatting of all possible valid examples:
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
			self.assertEqual(postcodes.formatPostCode(unformated), formated)


	def test_format_incorrect(self):
		
		"""
		This test case demonstrates formatting of all possible invalid examples:
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
		# condition#2
		condition2 = [('QA9A 9AAA','AA9A 9AA'),('VA9A 9AAA','AA9A 9AA'),('XA9A 9AAA','AA9A 9AA')]

		# condition#3
		condition3 = [('AI9A 9AAA','AA9A 9AA'),('AJ9A 9AAA','AA9A 9AA'),('AZ9A 9AAA','AA9A 9AA')]


		# condition#4
		# ILMNOQRVXYZ = LETTERS - ABCDEFGHJKPSTUW
		condition4 = [("A9"+val+" 9AA","AA9 9AA") for val in "ILMNOQRVXYZ"]


		# condition#5
		# CDFGIJKLOQSTUZ = LETTERS - ABEHMNPRVWXY		
		condition5 = [("AA9"+val+" 9AA","AA9A 9AA") for val in "CDFGIJKLOQSTUZ"]

		# condition#6
		# As it says on final two positions, either one of them would do 
		condition6 = [("A9A 9"+val+""+val,"AA9A 9AA") for val in "CIKMOV"]

		# condition#1 and Generic cases
		cases = [("AA999 9AA","A99 9AA"),("A999 9AA","AA9 9AA"),("AAA99 9AA","AA99 9AA"),("A999 9AA","AA99 9AA"),
				('AAAA 9AA','AA9A 9AA'),('AA9A 99A','AA9A 9AA'),('AA9A AAA','AA9A 9AA'),('AA9A 9AAA','AA9A 9AA'),
				("AA999 9AA","A99 9AA"),("A999 9AA","AA9 9AA"),("AAA99 9AA","AA99 9AA"),("A999 9AA","AA99 9AA"),
				('AAAA 9AA','AA9A 9AA'),('AA9A 99A','AA9A 9AA'),('AA9A AAA','AA9A 9AA'),('AA9A 9AAA','AA9A 9AA'),
				('QA9A 9AAA','AA9A 9AA'),('VA9A 9AAA','AA9A 9AA'),('XA9A 9AAA','AA9A 9AA')]

		cases = cases + condition2 + condition3 +condition4 + condition5 + condition6		
		for unformated,formated in cases:
			with self.assertRaises(postcodes.PostCodeError):
				postcodes.formatPostCode(unformated)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(PostCodeFormatTestSuite)
	unittest.TextTestRunner(verbosity=2).run(suite)