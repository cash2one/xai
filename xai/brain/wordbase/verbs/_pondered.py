

from xai.brain.wordbase.verbs._ponder import _PONDER

#calss header
class _PONDERED(_PONDER, ):
	def __init__(self,): 
		_PONDER.__init__(self)
		self.name = "PONDERED"
		self.specie = 'verbs'
		self.basic = "ponder"
		self.jsondata = {}
