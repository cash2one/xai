

from xai.brain.wordbase.nouns._pause import _PAUSE

#calss header
class _PAUSED(_PAUSE, ):
	def __init__(self,): 
		_PAUSE.__init__(self)
		self.name = "PAUSED"
		self.specie = 'nouns'
		self.basic = "pause"
		self.jsondata = {}
