

from xai.brain.wordbase.verbs._forecast import _FORECAST

#calss header
class _FORECASTED(_FORECAST, ):
	def __init__(self,): 
		_FORECAST.__init__(self)
		self.name = "FORECASTED"
		self.specie = 'verbs'
		self.basic = "forecast"
		self.jsondata = {}
