

from xai.brain.wordbase.verbs._dampen import _DAMPEN

#calss header
class _DAMPENED(_DAMPEN, ):
	def __init__(self,): 
		_DAMPEN.__init__(self)
		self.name = "DAMPENED"
		self.specie = 'verbs'
		self.basic = "dampen"
		self.jsondata = {}
