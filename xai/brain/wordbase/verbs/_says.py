

from xai.brain.wordbase.verbs._say import _SAY

#calss header
class _SAYS(_SAY, ):
	def __init__(self,): 
		_SAY.__init__(self)
		self.name = "SAYS"
		self.specie = 'verbs'
		self.basic = "say"
		self.jsondata = {}
