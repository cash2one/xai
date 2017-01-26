

from xai.brain.wordbase.adjectives._comparative import _COMPARATIVE

#calss header
class _COMPARATIVES(_COMPARATIVE, ):
	def __init__(self,): 
		_COMPARATIVE.__init__(self)
		self.name = "COMPARATIVES"
		self.specie = 'adjectives'
		self.basic = "comparative"
		self.jsondata = {}
