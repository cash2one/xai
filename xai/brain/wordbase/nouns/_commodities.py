

from xai.brain.wordbase.nouns._commodity import _COMMODITY

#calss header
class _COMMODITIES(_COMMODITY, ):
	def __init__(self,): 
		_COMMODITY.__init__(self)
		self.name = "COMMODITIES"
		self.specie = 'nouns'
		self.basic = "commodity"
		self.jsondata = {}
