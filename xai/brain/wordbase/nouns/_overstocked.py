

from xai.brain.wordbase.nouns._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKED(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKED"
		self.specie = 'nouns'
		self.basic = "overstock"
		self.jsondata = {}
