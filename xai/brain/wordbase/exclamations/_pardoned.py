

from xai.brain.wordbase.exclamations._pardon import _PARDON

#calss header
class _PARDONED(_PARDON, ):
	def __init__(self,): 
		_PARDON.__init__(self)
		self.name = "PARDONED"
		self.specie = 'exclamations'
		self.basic = "pardon"
		self.jsondata = {}
