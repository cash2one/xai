

from xai.brain.wordbase.adverbs._cheap import _CHEAP

#calss header
class _CHEAPER(_CHEAP, ):
	def __init__(self,): 
		_CHEAP.__init__(self)
		self.name = "CHEAPER"
		self.specie = 'adverbs'
		self.basic = "cheap"
		self.jsondata = {}
