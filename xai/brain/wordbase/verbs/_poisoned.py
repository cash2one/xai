

from xai.brain.wordbase.verbs._poison import _POISON

#calss header
class _POISONED(_POISON, ):
	def __init__(self,): 
		_POISON.__init__(self)
		self.name = "POISONED"
		self.specie = 'verbs'
		self.basic = "poison"
		self.jsondata = {}
