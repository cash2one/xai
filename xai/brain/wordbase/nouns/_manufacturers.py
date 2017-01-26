

from xai.brain.wordbase.nouns._manufacturer import _MANUFACTURER

#calss header
class _MANUFACTURERS(_MANUFACTURER, ):
	def __init__(self,): 
		_MANUFACTURER.__init__(self)
		self.name = "MANUFACTURERS"
		self.specie = 'nouns'
		self.basic = "manufacturer"
		self.jsondata = {}
