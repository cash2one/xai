

from xai.brain.wordbase.nouns._quantity import _QUANTITY

#calss header
class _QUANTITIES(_QUANTITY, ):
	def __init__(self,): 
		_QUANTITY.__init__(self)
		self.name = "QUANTITIES"
		self.specie = 'nouns'
		self.basic = "quantity"
		self.jsondata = {}
