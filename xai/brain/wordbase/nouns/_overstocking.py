

from xai.brain.wordbase.nouns._overstock import _OVERSTOCK

#calss header
class _OVERSTOCKING(_OVERSTOCK, ):
	def __init__(self,): 
		_OVERSTOCK.__init__(self)
		self.name = "OVERSTOCKING"
		self.specie = 'nouns'
		self.basic = "overstock"
		self.jsondata = {}
