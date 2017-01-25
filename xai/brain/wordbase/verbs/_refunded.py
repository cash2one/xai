

from xai.brain.wordbase.verbs._refund import _REFUND

#calss header
class _REFUNDED(_REFUND, ):
	def __init__(self,): 
		_REFUND.__init__(self)
		self.name = "REFUNDED"
		self.specie = 'verbs'
		self.basic = "refund"
		self.jsondata = {}
