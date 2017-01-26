

from xai.brain.wordbase.verbs._unlearn import _UNLEARN

#calss header
class _UNLEARNING(_UNLEARN, ):
	def __init__(self,): 
		_UNLEARN.__init__(self)
		self.name = "UNLEARNING"
		self.specie = 'verbs'
		self.basic = "unlearn"
		self.jsondata = {}
