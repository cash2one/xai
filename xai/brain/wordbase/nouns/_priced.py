

from xai.brain.wordbase.nouns._price import _PRICE

#calss header
class _PRICED(_PRICE, ):
	def __init__(self,): 
		_PRICE.__init__(self)
		self.name = "PRICED"
		self.specie = 'nouns'
		self.basic = "price"
		self.jsondata = {}
