

from xai.brain.wordbase.verbs._maltreat import _MALTREAT

#calss header
class _MALTREATING(_MALTREAT, ):
	def __init__(self,): 
		_MALTREAT.__init__(self)
		self.name = "MALTREATING"
		self.specie = 'verbs'
		self.basic = "maltreat"
		self.jsondata = {}
