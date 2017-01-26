

from xai.brain.wordbase.nouns._reference import _REFERENCE

#calss header
class _REFERENCED(_REFERENCE, ):
	def __init__(self,): 
		_REFERENCE.__init__(self)
		self.name = "REFERENCED"
		self.specie = 'nouns'
		self.basic = "reference"
		self.jsondata = {}
