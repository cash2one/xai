

from xai.brain.wordbase.verbs._maltreat import _MALTREAT

#calss header
class _MALTREATS(_MALTREAT, ):
	def __init__(self,): 
		_MALTREAT.__init__(self)
		self.name = "MALTREATS"
		self.specie = 'verbs'
		self.basic = "maltreat"
		self.jsondata = {}
