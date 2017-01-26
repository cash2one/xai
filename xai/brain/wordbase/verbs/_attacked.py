

from xai.brain.wordbase.verbs._attack import _ATTACK

#calss header
class _ATTACKED(_ATTACK, ):
	def __init__(self,): 
		_ATTACK.__init__(self)
		self.name = "ATTACKED"
		self.specie = 'verbs'
		self.basic = "attack"
		self.jsondata = {}
