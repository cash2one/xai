

from xai.brain.wordbase.adjectives._fuzzy import _FUZZY

#calss header
class _FUZZIER(_FUZZY, ):
	def __init__(self,): 
		_FUZZY.__init__(self)
		self.name = "FUZZIER"
		self.specie = 'adjectives'
		self.basic = "fuzzy"
		self.jsondata = {}
