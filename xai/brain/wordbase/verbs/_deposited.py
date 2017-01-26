

from xai.brain.wordbase.verbs._deposit import _DEPOSIT

#calss header
class _DEPOSITED(_DEPOSIT, ):
	def __init__(self,): 
		_DEPOSIT.__init__(self)
		self.name = "DEPOSITED"
		self.specie = 'verbs'
		self.basic = "deposit"
		self.jsondata = {}
