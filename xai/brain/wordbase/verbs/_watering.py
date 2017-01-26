

from xai.brain.wordbase.verbs._water import _WATER

#calss header
class _WATERING(_WATER, ):
	def __init__(self,): 
		_WATER.__init__(self)
		self.name = "WATERING"
		self.specie = 'verbs'
		self.basic = "water"
		self.jsondata = {}
