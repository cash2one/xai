

from xai.brain.wordbase.verbs._concede import _CONCEDE

#calss header
class _CONCEDING(_CONCEDE, ):
	def __init__(self,): 
		_CONCEDE.__init__(self)
		self.name = "CONCEDING"
		self.specie = 'verbs'
		self.basic = "concede"
		self.jsondata = {}
