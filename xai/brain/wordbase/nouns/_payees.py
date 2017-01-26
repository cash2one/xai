

from xai.brain.wordbase.nouns._payee import _PAYEE

#calss header
class _PAYEES(_PAYEE, ):
	def __init__(self,): 
		_PAYEE.__init__(self)
		self.name = "PAYEES"
		self.specie = 'nouns'
		self.basic = "payee"
		self.jsondata = {}
