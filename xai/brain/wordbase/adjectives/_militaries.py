

from xai.brain.wordbase.adjectives._military import _MILITARY

#calss header
class _MILITARIES(_MILITARY, ):
	def __init__(self,): 
		_MILITARY.__init__(self)
		self.name = "MILITARIES"
		self.specie = 'adjectives'
		self.basic = "military"
		self.jsondata = {}
