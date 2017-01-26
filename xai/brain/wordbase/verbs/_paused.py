

from xai.brain.wordbase.verbs._pause import _PAUSE

#calss header
class _PAUSED(_PAUSE, ):
	def __init__(self,): 
		_PAUSE.__init__(self)
		self.name = "PAUSED"
		self.specie = 'verbs'
		self.basic = "pause"
		self.jsondata = {}
