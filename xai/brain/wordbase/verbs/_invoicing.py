

from xai.brain.wordbase.verbs._invoice import _INVOICE

#calss header
class _INVOICING(_INVOICE, ):
	def __init__(self,): 
		_INVOICE.__init__(self)
		self.name = "INVOICING"
		self.specie = 'verbs'
		self.basic = "invoice"
		self.jsondata = {}
