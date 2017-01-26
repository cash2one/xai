

from xai.brain.wordbase.nouns._homicide import _HOMICIDE

#calss header
class _HOMICIDES(_HOMICIDE, ):
	def __init__(self,): 
		_HOMICIDE.__init__(self)
		self.name = "HOMICIDES"
		self.specie = 'nouns'
		self.basic = "homicide"
		self.jsondata = {}
