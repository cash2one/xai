

from xai.brain.wordbase.verbs._filch import _FILCH

#calss header
class _FILCHED(_FILCH, ):
	def __init__(self,): 
		_FILCH.__init__(self)
		self.name = "FILCHED"
		self.specie = 'verbs'
		self.basic = "filch"
		self.jsondata = {}
