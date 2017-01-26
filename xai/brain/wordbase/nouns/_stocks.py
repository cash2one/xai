

from xai.brain.wordbase.nouns._stock import _STOCK

#calss header
class _STOCKS(_STOCK, ):
	def __init__(self,): 
		_STOCK.__init__(self)
		self.name = "STOCKS"
		self.specie = 'nouns'
		self.basic = "stock"
		self.jsondata = {}
