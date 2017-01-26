

from xai.brain.wordbase.nouns._inaccuracy import _INACCURACY

#calss header
class _INACCURACIES(_INACCURACY, ):
	def __init__(self,): 
		_INACCURACY.__init__(self)
		self.name = "INACCURACIES"
		self.specie = 'nouns'
		self.basic = "inaccuracy"
		self.jsondata = {}
