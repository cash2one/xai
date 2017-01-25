

from xai.brain.wordbase.adjectives._unknown import _UNKNOWN

#calss header
class _UNKNOWNS(_UNKNOWN, ):
	def __init__(self,): 
		_UNKNOWN.__init__(self)
		self.name = "UNKNOWNS"
		self.specie = 'adjectives'
		self.basic = "unknown"
		self.jsondata = {}
