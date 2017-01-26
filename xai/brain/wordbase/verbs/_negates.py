

from xai.brain.wordbase.verbs._negate import _NEGATE

#calss header
class _NEGATES(_NEGATE, ):
	def __init__(self,): 
		_NEGATE.__init__(self)
		self.name = "NEGATES"
		self.specie = 'verbs'
		self.basic = "negate"
		self.jsondata = {}
