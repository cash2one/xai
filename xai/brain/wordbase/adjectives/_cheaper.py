

from xai.brain.wordbase.adjectives._cheap import _CHEAP

#calss header
class _CHEAPER(_CHEAP, ):
	def __init__(self,): 
		_CHEAP.__init__(self)
		self.name = "CHEAPER"
		self.specie = 'adjectives'
		self.basic = "cheap"
		self.jsondata = {}
