

from xai.brain.wordbase.adverbs._cheap import _CHEAP

#calss header
class _CHEAPEST(_CHEAP, ):
	def __init__(self,): 
		_CHEAP.__init__(self)
		self.name = "CHEAPEST"
		self.specie = 'adverbs'
		self.basic = "cheap"
		self.jsondata = {}
