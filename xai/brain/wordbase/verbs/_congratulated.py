

from xai.brain.wordbase.verbs._congratulate import _CONGRATULATE

#calss header
class _CONGRATULATED(_CONGRATULATE, ):
	def __init__(self,): 
		_CONGRATULATE.__init__(self)
		self.name = "CONGRATULATED"
		self.specie = 'verbs'
		self.basic = "congratulate"
		self.jsondata = {}
