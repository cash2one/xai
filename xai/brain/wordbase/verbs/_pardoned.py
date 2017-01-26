

from xai.brain.wordbase.verbs._pardon import _PARDON

#calss header
class _PARDONED(_PARDON, ):
	def __init__(self,): 
		_PARDON.__init__(self)
		self.name = "PARDONED"
		self.specie = 'verbs'
		self.basic = "pardon"
		self.jsondata = {}
