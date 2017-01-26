

from xai.brain.wordbase.nouns._cleric import _CLERIC

#calss header
class _CLERICS(_CLERIC, ):
	def __init__(self,): 
		_CLERIC.__init__(self)
		self.name = "CLERICS"
		self.specie = 'nouns'
		self.basic = "cleric"
		self.jsondata = {}
