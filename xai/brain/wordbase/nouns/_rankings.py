

from xai.brain.wordbase.nouns._ranking import _RANKING

#calss header
class _RANKINGS(_RANKING, ):
	def __init__(self,): 
		_RANKING.__init__(self)
		self.name = "RANKINGS"
		self.specie = 'nouns'
		self.basic = "ranking"
		self.jsondata = {}
