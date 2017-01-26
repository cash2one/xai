

from xai.brain.wordbase.adjectives._probable import _PROBABLE

#calss header
class _PROBABLES(_PROBABLE, ):
	def __init__(self,): 
		_PROBABLE.__init__(self)
		self.name = "PROBABLES"
		self.specie = 'adjectives'
		self.basic = "probable"
		self.jsondata = {}
