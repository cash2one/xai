

from xai.brain.wordbase.nouns._weather import _WEATHER

#calss header
class _WEATHERED(_WEATHER, ):
	def __init__(self,): 
		_WEATHER.__init__(self)
		self.name = "WEATHERED"
		self.specie = 'nouns'
		self.basic = "weather"
		self.jsondata = {}
