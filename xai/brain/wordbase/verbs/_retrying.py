

from xai.brain.wordbase.verbs._retry import _RETRY

#calss header
class _RETRYING(_RETRY, ):
	def __init__(self,): 
		_RETRY.__init__(self)
		self.name = "RETRYING"
		self.specie = 'verbs'
		self.basic = "retry"
		self.jsondata = {}
