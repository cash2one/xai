

from xai.brain.wordbase.verbs._empty import _EMPTY

#calss header
class _EMPTIED(_EMPTY, ):
	def __init__(self,): 
		_EMPTY.__init__(self)
		self.name = "EMPTIED"
		self.specie = 'verbs'
		self.basic = "empty"
		self.jsondata = {}
