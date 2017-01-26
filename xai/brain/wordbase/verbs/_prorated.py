

from xai.brain.wordbase.verbs._prorate import _PRORATE

#calss header
class _PRORATED(_PRORATE, ):
	def __init__(self,): 
		_PRORATE.__init__(self)
		self.name = "PRORATED"
		self.specie = 'verbs'
		self.basic = "prorate"
		self.jsondata = {}
