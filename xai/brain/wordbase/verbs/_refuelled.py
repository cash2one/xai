

from xai.brain.wordbase.verbs._refuel import _REFUEL

#calss header
class _REFUELLED(_REFUEL, ):
	def __init__(self,): 
		_REFUEL.__init__(self)
		self.name = "REFUELLED"
		self.specie = 'verbs'
		self.basic = "refuel"
		self.jsondata = {}
