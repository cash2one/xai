

from xai.brain.wordbase.verbs._concede import _CONCEDE

#calss header
class _CONCEDED(_CONCEDE, ):
	def __init__(self,): 
		_CONCEDE.__init__(self)
		self.name = "CONCEDED"
		self.specie = 'verbs'
		self.basic = "concede"
		self.jsondata = {}
