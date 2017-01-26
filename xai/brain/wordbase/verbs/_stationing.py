

from xai.brain.wordbase.verbs._station import _STATION

#calss header
class _STATIONING(_STATION, ):
	def __init__(self,): 
		_STATION.__init__(self)
		self.name = "STATIONING"
		self.specie = 'verbs'
		self.basic = "station"
		self.jsondata = {}
