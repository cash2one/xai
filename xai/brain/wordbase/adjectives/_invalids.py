

from xai.brain.wordbase.adjectives._invalid import _INVALID

#calss header
class _INVALIDS(_INVALID, ):
	def __init__(self,): 
		_INVALID.__init__(self)
		self.name = "INVALIDS"
		self.specie = 'adjectives'
		self.basic = "invalid"
		self.jsondata = {}
