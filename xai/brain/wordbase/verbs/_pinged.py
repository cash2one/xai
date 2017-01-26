

from xai.brain.wordbase.verbs._ping import _PING

#calss header
class _PINGED(_PING, ):
	def __init__(self,): 
		_PING.__init__(self)
		self.name = "PINGED"
		self.specie = 'verbs'
		self.basic = "ping"
		self.jsondata = {}
