

from xai.brain.wordbase.adjectives._rank import _RANK

#calss header
class _RANKED(_RANK, ):
	def __init__(self,): 
		_RANK.__init__(self)
		self.name = "RANKED"
		self.specie = 'adjectives'
		self.basic = "rank"
		self.jsondata = {}
