

from xai.brain.wordbase.verbs._compute import _COMPUTE

#calss header
class _COMPUTES(_COMPUTE, ):
	def __init__(self,): 
		_COMPUTE.__init__(self)
		self.name = "COMPUTES"
		self.specie = 'verbs'
		self.basic = "compute"
		self.jsondata = {}
