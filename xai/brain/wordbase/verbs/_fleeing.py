

from xai.brain.wordbase.verbs._flee import _FLEE

#calss header
class _FLEEING(_FLEE, ):
	def __init__(self,): 
		_FLEE.__init__(self)
		self.name = "FLEEING"
		self.specie = 'verbs'
		self.basic = "flee"
		self.jsondata = {}
