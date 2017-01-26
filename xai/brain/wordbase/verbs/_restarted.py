

from xai.brain.wordbase.verbs._restart import _RESTART

#calss header
class _RESTARTED(_RESTART, ):
	def __init__(self,): 
		_RESTART.__init__(self)
		self.name = "RESTARTED"
		self.specie = 'verbs'
		self.basic = "restart"
		self.jsondata = {}
