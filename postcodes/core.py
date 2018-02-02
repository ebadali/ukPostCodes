# -*- coding: utf-8 -*-
"""Example Google style docstrings.

This module performs validation and formats the uk post codes.
Postcode format is:

									POSTCODE
				Outward Code	      |          Inward Code
	Postcode Area :	Postcode District |	Postcode Sector : Postcode Unit

Example:

	This module can be used by importing it into any existing script
        from postcodes import validatePostCode,formatPostCode

		validatePostCode(postcode)
		formatPostCode(postcode)

Attributes:
    regex (Object): 
		Regular expression for matching with the Uk post codes
	
Todo:
    * Integrate RE's for Uk speacial post codes cases 
    * Add Command line argument interpreter

"""

from customexceptions import PostCodeError
import re

regex = re.compile('^(([gG][iI][rR] {0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9][abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2}))$')

# Few RE's to match certain edge cases
# conditionSixRe = re.compile('^.{0}[^QVX]')
# conditionSevenRe = re.compile('^.{1}[^IJZ]')
# conditionEightRe = re.compile('^(?=[a-zA-Z]\d[a-zA-Z])(?=.{2}[ABCDEFGHJKPSTUW])')
# conditionNineRe = re.compile('(?=.*[a-zA-Z][a-zA-Z]\d[a-zA-Z])(?=.{3}[ABEHMNPRVWXY])')



def getOutwardPart(postcode):
	"""Returns the Outward part of the postcode
	
	Description
	-----------

	Extract the outward part of from the postcode
	It will NOT neccesory gives the correct outward code ! 
	Infact it only extracts between two and four characters long string
	The outward code is the part of the postcode before the single space in the middle.
	
	Examples
	--------
	Examples of outward codes include 
	"L1", "W1A", "RH1", "RH10" or "SE1P". 
	A few outward codes are non-geographic, not divulging where mail is to be sent.

	Attributes
	----------
	postcode : string
		The postcode

	Returns
	-------
	String
		Three character long string as Inward part

	Raises
	------
	Exception: Raises exception if the given postcode is of invalid length; length less than 5 
	"""
	
	# Figuring out the correct length of Outward code
	# as inward code is always of length 3    
	length = len(postcode)
	if length < 5:
		raise Exception('Invalid outward part')    

	return postcode[0:length-3]


def getInwardPart(postcode):
	"""Returns the Inward part of the postcode

	Description
	-----------
	Extract the Inward part of from the postcode
	It will not neccesory gives the correct Inward code.
	Infact it only extracts three characters long string.
	The inward code is the part of the postcode after the single space in the middle.
	The inward code assists in the delivery of post within a postal district. 
	
	Examples
	--------
	Examples of inward codes include: 
	"0NY", "7GZ", "7HF", or "8JQ"



	Attributes
	----------
	postcode : string
		The postcode

	Returns
	-------
	String
		Three character long string as Inward part

	Raises
	------
	Exception: Raises exception if the given postcode is of invalid length


	"""


	length = len(postcode)
	if length < 5:
		raise Exception('Invalid Inward part')    

	return postcode[length-3:]


def formatPostCode(code):
	"""Formats the Postcode
	
	Description
	-----------
		
	where Postcode is made of two major parts:
	Outward code space Inward code; Such as : {{Outward code}} {{Inward code}}
	Where,
	InwardCode = 3 chartacter long,
	with a single digit at first position and two letters following that.

	OutwardCode = 3 chartacter long,
	with a single digit at first position and two letters following that.    
	example:
	AA9A 9AA
	A9A 9AA

	Attributes
	----------
	code : string
		Post code in String 

	Returns
	-------
	String
		Formatted and validated postcode.

	

	"""

	# Removes all spaces.
	trimmedCode = re.sub(' ','',code)
	try:
		# Get Inward and Outward code
		formattedCode = getOutwardPart(trimmedCode) +" "+getInwardPart(trimmedCode)
		# Now validatePostCode the postCode   
		if not validatePostCode(formattedCode):
			raise Exception('Invalid Post Code Format')
	except Exception as ex:
		raise PostCodeError(str(ex))
			
	return formattedCode


def validatePostCode(text):
    
	""" Validates the uk postcode
	Description
	-----------
	This function validates the Uk Postcode by matching it against a Regular Expression.
	Where Postcode is made of two major parts:
	Outward code space Inward code; Such as : {{Outward code}} {{Inward code}}
	Where,
	InwardCode = 3 chartacter long,
	with a single digit at first position and two letters following that.

	OutwardCode = 3 chartacter long,
	with a single digit at first position and two letters following that.    

	Conditions
	---------
	This function take special care of the following conditions

	-condition#1 all formats end with 9AA
	-condition#2 The letters QVX are NOT used in the first position.
	-condition#3 The letters IJZ are NOT used in the second position.
	-condition#4 The only letters to appear in the third position are ABCDEFGHJKPSTUW when the structure starts with A9A.
	-condition#5 The only letters to appear in the fourth position are ABEHMNPRVWXY when the structure starts with AA9A.
	-condition#6 The final two letters Does NOT use the letters CIKMOV, so as not to resemble digits or each other when hand-written.
	-condition#7 end with 9AA
	-condition#8 Areas with only single-digit districts
	-condition#9 Areas with only double-digit districts
	-condition#10 Areas with a district 0
	
	
	Attributes
	----------
	code : string
		Post code in String 

	Returns
	-------
	boolean
		true if postcode is validated otherwise false
	
	"""

	# Matching the post code with the Uk post code 
	# regular expression, return true if it matches
	# false otherwise
	return True if regex.match(text) else False