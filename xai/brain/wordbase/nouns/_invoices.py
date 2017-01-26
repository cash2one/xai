

from xai.brain.wordbase.nouns._invoice import _INVOICE

#calss header
class _INVOICES(_INVOICE, ):
	def __init__(self,): 
		_INVOICE.__init__(self)
		self.name = "INVOICES"
		self.specie = 'nouns'
		self.basic = "invoice"
		self.jsondata = {}
