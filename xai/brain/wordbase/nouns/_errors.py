

from xai.brain.wordbase.nouns._error import _ERROR

#calss header
class _ERRORS(_ERROR, ):
	def __init__(self,): 
		_ERROR.__init__(self)
		self.name = "ERRORS"
		self.specie = 'nouns'
		self.basic = "error"
		self.jsondata = {}
