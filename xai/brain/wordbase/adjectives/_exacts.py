

from xai.brain.wordbase.adjectives._exact import _EXACT

#calss header
class _EXACTS(_EXACT, ):
	def __init__(self,): 
		_EXACT.__init__(self)
		self.name = "EXACTS"
		self.specie = 'adjectives'
		self.basic = "exact"
		self.jsondata = {}
