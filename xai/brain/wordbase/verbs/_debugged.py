

from xai.brain.wordbase.verbs._debug import _DEBUG

#calss header
class _DEBUGGED(_DEBUG, ):
	def __init__(self,): 
		_DEBUG.__init__(self)
		self.name = "DEBUGGED"
		self.specie = 'verbs'
		self.basic = "debug"
		self.jsondata = {}
