

from xai.brain.wordbase.verbs._reject import _REJECT

#calss header
class _REJECTS(_REJECT, ):
	def __init__(self,): 
		_REJECT.__init__(self)
		self.name = "REJECTS"
		self.specie = 'verbs'
		self.basic = "reject"
		self.jsondata = {}
