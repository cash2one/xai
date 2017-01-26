

from xai.brain.wordbase.verbs._terminate import _TERMINATE

#calss header
class _TERMINATED(_TERMINATE, ):
	def __init__(self,): 
		_TERMINATE.__init__(self)
		self.name = "TERMINATED"
		self.specie = 'verbs'
		self.basic = "terminate"
		self.jsondata = {}
