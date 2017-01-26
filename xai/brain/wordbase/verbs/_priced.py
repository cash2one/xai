

from xai.brain.wordbase.verbs._price import _PRICE

#calss header
class _PRICED(_PRICE, ):
	def __init__(self,): 
		_PRICE.__init__(self)
		self.name = "PRICED"
		self.specie = 'verbs'
		self.basic = "price"
		self.jsondata = {}
