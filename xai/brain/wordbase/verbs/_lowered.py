

from xai.brain.wordbase.verbs._lower import _LOWER

#calss header
class _LOWERED(_LOWER, ):
	def __init__(self,): 
		_LOWER.__init__(self)
		self.name = "LOWERED"
		self.specie = 'verbs'
		self.basic = "lower"
		self.jsondata = {}
