

from xai.brain.wordbase.adjectives._ranking import _RANKING

#calss header
class _RANKINGS(_RANKING, ):
	def __init__(self,): 
		_RANKING.__init__(self)
		self.name = "RANKINGS"
		self.specie = 'adjectives'
		self.basic = "ranking"
		self.jsondata = {}
