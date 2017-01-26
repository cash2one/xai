

from xai.brain.wordbase.verbs._stop import _STOP

#calss header
class _STOPPED(_STOP, ):
	def __init__(self,): 
		_STOP.__init__(self)
		self.name = "STOPPED"
		self.specie = 'verbs'
		self.basic = "stop"
		self.jsondata = {}
