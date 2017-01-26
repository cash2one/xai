

from xai.brain.wordbase.adjectives._weak import _WEAK

#calss header
class _WEAKER(_WEAK, ):
	def __init__(self,): 
		_WEAK.__init__(self)
		self.name = "WEAKER"
		self.specie = 'adjectives'
		self.basic = "weak"
		self.jsondata = {}
