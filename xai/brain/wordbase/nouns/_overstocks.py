

from xai.brain.wordbase.nouns._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKS(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKS"
		self.specie = 'nouns'
		self.basic = "overstock"
		self.jsondata = {}
