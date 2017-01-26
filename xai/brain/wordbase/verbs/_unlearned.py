

from xai.brain.wordbase.verbs._unlearn import _UNLEARN

#calss header
class _UNLEARNED(_UNLEARN, ):
	def __init__(self,): 
		_UNLEARN.__init__(self)
		self.name = "UNLEARNED"
		self.specie = 'verbs'
		self.basic = "unlearn"
		self.jsondata = {}
