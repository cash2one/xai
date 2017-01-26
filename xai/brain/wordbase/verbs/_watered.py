

from xai.brain.wordbase.verbs._water import _WATER

#calss header
class _WATERED(_WATER, ):
	def __init__(self,): 
		_WATER.__init__(self)
		self.name = "WATERED"
		self.specie = 'verbs'
		self.basic = "water"
		self.jsondata = {}
