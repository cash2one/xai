

from xai.brain.wordbase.verbs._terminate import _TERMINATE

#calss header
class _TERMINATING(_TERMINATE, ):
	def __init__(self,): 
		_TERMINATE.__init__(self)
		self.name = "TERMINATING"
		self.specie = 'verbs'
		self.basic = "terminate"
		self.jsondata = {}
