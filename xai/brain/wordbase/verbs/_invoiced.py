

from xai.brain.wordbase.verbs._invoice import _INVOICE

#calss header
class _INVOICED(_INVOICE, ):
	def __init__(self,): 
		_INVOICE.__init__(self)
		self.name = "INVOICED"
		self.specie = 'verbs'
		self.basic = "invoice"
		self.jsondata = {}
