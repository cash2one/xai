

from xai.brain.wordbase.nouns._subtotal import _SUBTOTAL

#calss header
class _SUBTOTALS(_SUBTOTAL, ):
	def __init__(self,): 
		_SUBTOTAL.__init__(self)
		self.name = "SUBTOTALS"
		self.specie = 'nouns'
		self.basic = "subtotal"
		self.jsondata = {}
