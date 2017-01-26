

from xai.brain.wordbase.verbs._transact import _TRANSACT

#calss header
class _TRANSACTED(_TRANSACT, ):
	def __init__(self,): 
		_TRANSACT.__init__(self)
		self.name = "TRANSACTED"
		self.specie = 'verbs'
		self.basic = "transact"
		self.jsondata = {}
