

from xai.brain.wordbase.verbs._cure import _CURE

#calss header
class _CURED(_CURE, ):
	def __init__(self,): 
		_CURE.__init__(self)
		self.name = "CURED"
		self.specie = 'verbs'
		self.basic = "cure"
		self.jsondata = {}
