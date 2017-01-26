

from xai.brain.wordbase.verbs._attack import _ATTACK

#calss header
class _ATTACKING(_ATTACK, ):
	def __init__(self,): 
		_ATTACK.__init__(self)
		self.name = "ATTACKING"
		self.specie = 'verbs'
		self.basic = "attack"
		self.jsondata = {}
