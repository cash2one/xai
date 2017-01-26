

from xai.brain.wordbase.verbs._terminate import _TERMINATE

#calss header
class _TERMINATES(_TERMINATE, ):
	def __init__(self,): 
		_TERMINATE.__init__(self)
		self.name = "TERMINATES"
		self.specie = 'verbs'
		self.basic = "terminate"
		self.jsondata = {}
