# -*- coding: utf-8 -*-
import helpers


import re


pattern = '^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'

# Captures Last 3 characters
inwardCodePattern = r'[0-9][a-zA-Z]{2}$'

# Captures First  two - four characters long
outwardCodePattern = r'^(\S{2,4})'

regex = re.compile(pattern)
inwardCodeRe = re.compile(inwardCodePattern)
inwardCodeRe = re.compile(inwardCodePattern)


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


def getOutwardPart(postcode):
    """
    Extract the outward part of from the postcode
    It will not neccesory gives the correct outward code ! 
    Infact it only extracts between two and four characters long string

    Attributes
    ----------
    postcode : string
        The postcode

    Returns
    -------
    int
        Description of anonymous integer return value.    

    The outward code is the part of the postcode before the single space in the middle.
    It is between two and four characters long. Examples of outward codes include 
    "L1", "W1A", "RH1", "RH10" or "SE1P". 
    A few outward codes are non-geographic, not divulging where mail is to be sent.
    """
    
    # Figuring out the correct length of Outward code
    # as inward code is always of length 3    
    length = len(postcode)
    if length < 5:
        raise Exception('Invalid outward part')    

    return postcode[0:length-3]


def getInwardPart(postcode):
    """
    Extract the Inward part of from the postcode
    It will not neccesory gives the correct Inward code ! 
    Infact it only extracts between two and four characters long string

    Attributes
    ----------
    postcode : string
        The postcode

    Returns
    -------
    int
        Description of anonymous integer return value.

    The inward code is the part of the postcode after the single space in the middle.
    It is three characters long. The inward code assists in the delivery of post within a postal district. 
    Examples of inward codes include "0NY", "7GZ", "7HF", or "8JQ"
    """


    length = len(postcode)
    if length < 5:
        raise Exception('Invalid Inward part')    

    return postcode[length-3:]


def format(code):
    """Formats the Postcode
    
        
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
    """

    # Removes all spaces.
    trimmedCode = re.sub(' ','',code)
    try:
        # Get Inward and Outward code
        formattedCode = getOutwardPart(trimmedCode) +" "+getInwardPart(trimmedCode)
        # Now validate the postCode   
        if not validate(formattedCode):
            raise Exception('Invalid Post Code')
    except Exception as ex:
        raise Exception(str(ex))
            
    return formattedCode

def validate(text):
    
   """
    Postcode format : 
                                    POSTCODE
                Outward Code	      |          Inward Code
    Postcode Area :	Postcode District |	Postcode Sector : Postcode Unit

   """
   return (regex.match(text))

print(validate('AA9A 9AA'))
print(validate('A9A 9AA'))
print(validate('A9 9AA'))
print(validate('A99 9AA'))
print(validate('AA9 9AA'))
print(validate('AA99 9AA'))


print(format('AA9A9AA'))
print(format('A9A9AA'))
print(format('A9 9AA'))
print(format('A99 9AA'))



a = ['AA99 9AA','AA9A9AA','as34243','2123']
for i in a:
    try:        
        print(format(i))
    except Exception as ex :
        print('error at ', i, ex)
