

from xai.brain.wordbase.verbs._manipulate import _MANIPULATE

#calss header
class _MANIPULATED(_MANIPULATE, ):
	def __init__(self,): 
		_MANIPULATE.__init__(self)
		self.name = "MANIPULATED"
		self.specie = 'verbs'
		self.basic = "manipulate"
		self.jsondata = {}
