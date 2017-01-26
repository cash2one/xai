

from xai.brain.wordbase.verbs._approve import _APPROVE

#calss header
class _APPROVES(_APPROVE, ):
	def __init__(self,): 
		_APPROVE.__init__(self)
		self.name = "APPROVES"
		self.specie = 'verbs'
		self.basic = "approve"
		self.jsondata = {}
