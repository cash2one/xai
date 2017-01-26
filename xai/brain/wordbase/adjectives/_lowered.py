

from xai.brain.wordbase.adjectives._lower import _LOWER

#calss header
class _LOWERED(_LOWER, ):
	def __init__(self,): 
		_LOWER.__init__(self)
		self.name = "LOWERED"
		self.specie = 'adjectives'
		self.basic = "lower"
		self.jsondata = {}
