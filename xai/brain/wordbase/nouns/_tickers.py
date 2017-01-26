

from xai.brain.wordbase.nouns._ticker import _TICKER

#calss header
class _TICKERS(_TICKER, ):
	def __init__(self,): 
		_TICKER.__init__(self)
		self.name = "TICKERS"
		self.specie = 'nouns'
		self.basic = "ticker"
		self.jsondata = {}
