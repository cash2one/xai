

from xai.brain.wordbase.verbs._tabulate import _TABULATE

#calss header
class _TABULATED(_TABULATE, ):
	def __init__(self,): 
		_TABULATE.__init__(self)
		self.name = "TABULATED"
		self.specie = 'verbs'
		self.basic = "tabulate"
		self.jsondata = {}
