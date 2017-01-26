

from xai.brain.wordbase.verbs._empty import _EMPTY

#calss header
class _EMPTIES(_EMPTY, ):
	def __init__(self,): 
		_EMPTY.__init__(self)
		self.name = "EMPTIES"
		self.specie = 'verbs'
		self.basic = "empty"
		self.jsondata = {}
