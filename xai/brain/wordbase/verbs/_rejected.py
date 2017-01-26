

from xai.brain.wordbase.verbs._reject import _REJECT

#calss header
class _REJECTED(_REJECT, ):
	def __init__(self,): 
		_REJECT.__init__(self)
		self.name = "REJECTED"
		self.specie = 'verbs'
		self.basic = "reject"
		self.jsondata = {}
