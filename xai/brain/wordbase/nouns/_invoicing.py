

from xai.brain.wordbase.nouns._invoice import _INVOICE

#calss header
class _INVOICING(_INVOICE, ):
	def __init__(self,): 
		_INVOICE.__init__(self)
		self.name = "INVOICING"
		self.specie = 'nouns'
		self.basic = "invoice"
		self.jsondata = {}
