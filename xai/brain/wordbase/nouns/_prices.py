

from xai.brain.wordbase.nouns._price import _PRICE

#calss header
class _PRICES(_PRICE, ):
	def __init__(self,): 
		_PRICE.__init__(self)
		self.name = "PRICES"
		self.specie = 'nouns'
		self.basic = "price"
		self.jsondata = {}
