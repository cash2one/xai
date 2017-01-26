

from xai.brain.wordbase.verbs._reject import _REJECT

#calss header
class _REJECTING(_REJECT, ):
	def __init__(self,): 
		_REJECT.__init__(self)
		self.name = "REJECTING"
		self.specie = 'verbs'
		self.basic = "reject"
		self.jsondata = {}
