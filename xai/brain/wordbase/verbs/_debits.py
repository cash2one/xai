

from xai.brain.wordbase.verbs._debit import _DEBIT

#calss header
class _DEBITS(_DEBIT, ):
	def __init__(self,): 
		_DEBIT.__init__(self)
		self.name = "DEBITS"
		self.specie = 'verbs'
		self.basic = "debit"
		self.jsondata = {}
