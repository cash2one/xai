

from xai.brain.wordbase.verbs._substitute import _SUBSTITUTE

#calss header
class _SUBSTITUTED(_SUBSTITUTE, ):
	def __init__(self,): 
		_SUBSTITUTE.__init__(self)
		self.name = "SUBSTITUTED"
		self.specie = 'verbs'
		self.basic = "substitute"
		self.jsondata = {}
