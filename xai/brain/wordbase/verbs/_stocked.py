

from xai.brain.wordbase.verbs._stock import _STOCK

#calss header
class _STOCKED(_STOCK, ):
	def __init__(self,): 
		_STOCK.__init__(self)
		self.name = "STOCKED"
		self.specie = 'verbs'
		self.basic = "stock"
		self.jsondata = {}
