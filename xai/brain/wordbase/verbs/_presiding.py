

from xai.brain.wordbase.verbs._preside import _PRESIDE

#calss header
class _PRESIDING(_PRESIDE, ):
	def __init__(self,): 
		_PRESIDE.__init__(self)
		self.name = "PRESIDING"
		self.specie = 'verbs'
		self.basic = "preside"
		self.jsondata = {}
