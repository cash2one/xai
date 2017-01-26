

from xai.brain.wordbase.nouns._weight import _WEIGHT

#calss header
class _WEIGHTED(_WEIGHT, ):
	def __init__(self,): 
		_WEIGHT.__init__(self)
		self.name = "WEIGHTED"
		self.specie = 'nouns'
		self.basic = "weight"
		self.jsondata = {}
