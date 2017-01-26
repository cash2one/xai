

from xai.brain.wordbase.nouns._trade import _TRADE

#calss header
class _TRADED(_TRADE, ):
	def __init__(self,): 
		_TRADE.__init__(self)
		self.name = "TRADED"
		self.specie = 'nouns'
		self.basic = "trade"
		self.jsondata = {}
