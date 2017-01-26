

from xai.brain.wordbase.nouns._tradesman import _TRADESMAN

#calss header
class _TRADESMEN(_TRADESMAN, ):
	def __init__(self,): 
		_TRADESMAN.__init__(self)
		self.name = "TRADESMEN"
		self.specie = 'nouns'
		self.basic = "tradesman"
		self.jsondata = {}
