

from xai.brain.wordbase.nouns._equity import _EQUITY

#calss header
class _EQUITIES(_EQUITY, ):
	def __init__(self,): 
		_EQUITY.__init__(self)
		self.name = "EQUITIES"
		self.specie = 'nouns'
		self.basic = "equity"
		self.jsondata = {}
