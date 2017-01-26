

from xai.brain.wordbase.nouns._empty import _EMPTY

#calss header
class _EMPTIES(_EMPTY, ):
	def __init__(self,): 
		_EMPTY.__init__(self)
		self.name = "EMPTIES"
		self.specie = 'nouns'
		self.basic = "empty"
		self.jsondata = {}
