

from xai.brain.wordbase.nouns._forecast import _FORECAST

#calss header
class _FORECASTS(_FORECAST, ):
	def __init__(self,): 
		_FORECAST.__init__(self)
		self.name = "FORECASTS"
		self.specie = 'nouns'
		self.basic = "forecast"
		self.jsondata = {}
