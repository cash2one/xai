

from xai.brain.wordbase.verbs._denude import _DENUDE

#calss header
class _DENUDED(_DENUDE, ):
	def __init__(self,): 
		_DENUDE.__init__(self)
		self.name = "DENUDED"
		self.specie = 'verbs'
		self.basic = "denude"
		self.jsondata = {}
