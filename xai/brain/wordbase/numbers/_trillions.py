

from xai.brain.wordbase.numbers._trillion import _TRILLION

#calss header
class _TRILLIONS(_TRILLION, ):
	def __init__(self,): 
		_TRILLION.__init__(self)
		self.name = "TRILLIONS"
		self.specie = 'numbers'
		self.basic = "trillion"
		self.jsondata = {}
