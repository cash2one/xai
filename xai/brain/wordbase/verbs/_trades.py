

from xai.brain.wordbase.verbs._trade import _TRADE

#calss header
class _TRADES(_TRADE, ):
	def __init__(self,): 
		_TRADE.__init__(self)
		self.name = "TRADES"
		self.specie = 'verbs'
		self.basic = "trade"
		self.jsondata = {}
