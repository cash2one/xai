

from xai.brain.wordbase.verbs._depopulate import _DEPOPULATE

#calss header
class _DEPOPULATED(_DEPOPULATE, ):
	def __init__(self,): 
		_DEPOPULATE.__init__(self)
		self.name = "DEPOPULATED"
		self.specie = 'verbs'
		self.basic = "depopulate"
		self.jsondata = {}
