

from xai.brain.wordbase.verbs._degrade import _DEGRADE

#calss header
class _DEGRADED(_DEGRADE, ):
	def __init__(self,): 
		_DEGRADE.__init__(self)
		self.name = "DEGRADED"
		self.specie = 'verbs'
		self.basic = "degrade"
		self.jsondata = {}
