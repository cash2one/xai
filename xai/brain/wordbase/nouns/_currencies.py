

from xai.brain.wordbase.nouns._currency import _CURRENCY

#calss header
class _CURRENCIES(_CURRENCY, ):
	def __init__(self,): 
		_CURRENCY.__init__(self)
		self.name = "CURRENCIES"
		self.specie = 'nouns'
		self.basic = "currency"
		self.jsondata = {}
