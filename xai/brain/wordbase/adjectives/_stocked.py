

from xai.brain.wordbase.adjectives._stock import _STOCK

#calss header
class _STOCKED(_STOCK, ):
	def __init__(self,): 
		_STOCK.__init__(self)
		self.name = "STOCKED"
		self.specie = 'adjectives'
		self.basic = "stock"
		self.jsondata = {}
