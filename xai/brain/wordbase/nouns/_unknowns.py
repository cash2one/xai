

from xai.brain.wordbase.nouns._unknown import _UNKNOWN

#calss header
class _UNKNOWNS(_UNKNOWN, ):
	def __init__(self,): 
		_UNKNOWN.__init__(self)
		self.name = "UNKNOWNS"
		self.specie = 'nouns'
		self.basic = "unknown"
		self.jsondata = {}
