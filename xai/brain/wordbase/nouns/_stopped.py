

from xai.brain.wordbase.nouns._stop import _STOP

#calss header
class _STOPPED(_STOP, ):
	def __init__(self,): 
		_STOP.__init__(self)
		self.name = "STOPPED"
		self.specie = 'nouns'
		self.basic = "stop"
		self.jsondata = {}
