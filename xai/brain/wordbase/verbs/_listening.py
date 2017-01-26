

from xai.brain.wordbase.verbs._listen import _LISTEN

#calss header
class _LISTENING(_LISTEN, ):
	def __init__(self,): 
		_LISTEN.__init__(self)
		self.name = "LISTENING"
		self.specie = 'verbs'
		self.basic = "listen"
		self.jsondata = {}
