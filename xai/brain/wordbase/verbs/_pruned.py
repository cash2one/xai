

from xai.brain.wordbase.verbs._prune import _PRUNE

#calss header
class _PRUNED(_PRUNE, ):
	def __init__(self,): 
		_PRUNE.__init__(self)
		self.name = "PRUNED"
		self.specie = 'verbs'
		self.basic = "prune"
		self.jsondata = {}
