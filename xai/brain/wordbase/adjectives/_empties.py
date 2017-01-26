

from xai.brain.wordbase.adjectives._empty import _EMPTY

#calss header
class _EMPTIES(_EMPTY, ):
	def __init__(self,): 
		_EMPTY.__init__(self)
		self.name = "EMPTIES"
		self.specie = 'adjectives'
		self.basic = "empty"
		self.jsondata = {}
