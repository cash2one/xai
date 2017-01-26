

from xai.brain.wordbase.verbs._gather import _GATHER

#calss header
class _GATHERED(_GATHER, ):
	def __init__(self,): 
		_GATHER.__init__(self)
		self.name = "GATHERED"
		self.specie = 'verbs'
		self.basic = "gather"
		self.jsondata = {}
