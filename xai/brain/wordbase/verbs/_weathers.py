

from xai.brain.wordbase.verbs._weather import _WEATHER

#calss header
class _WEATHERS(_WEATHER, ):
	def __init__(self,): 
		_WEATHER.__init__(self)
		self.name = "WEATHERS"
		self.specie = 'verbs'
		self.basic = "weather"
		self.jsondata = {}
