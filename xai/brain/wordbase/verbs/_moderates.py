

from xai.brain.wordbase.verbs._moderate import _MODERATE

#calss header
class _MODERATES(_MODERATE, ):
	def __init__(self,): 
		_MODERATE.__init__(self)
		self.name = "MODERATES"
		self.specie = 'verbs'
		self.basic = "moderate"
		self.jsondata = {}
