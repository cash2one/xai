

from xai.brain.wordbase.verbs._quit import _QUIT

#calss header
class _QUITTED(_QUIT, ):
	def __init__(self,): 
		_QUIT.__init__(self)
		self.name = "QUITTED"
		self.specie = 'verbs'
		self.basic = "quit"
		self.jsondata = {}
