

from xai.brain.wordbase.adjectives._trade import _TRADE

#calss header
class _TRADED(_TRADE, ):
	def __init__(self,): 
		_TRADE.__init__(self)
		self.name = "TRADED"
		self.specie = 'adjectives'
		self.basic = "trade"
		self.jsondata = {}
