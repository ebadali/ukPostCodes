
class PostCodeError(Exception):

	"""This Exception cast the Exception on Invalid Format inputs.

    Args:
        msg (str): Human readable string describing the exception.

    Attributes:
        msg (str): Human readable string describing the exception.
        
	"""
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)