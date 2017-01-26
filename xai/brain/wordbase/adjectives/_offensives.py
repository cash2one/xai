

from xai.brain.wordbase.adjectives._offensive import _OFFENSIVE

#calss header
class _OFFENSIVES(_OFFENSIVE, ):
	def __init__(self,): 
		_OFFENSIVE.__init__(self)
		self.name = "OFFENSIVES"
		self.specie = 'adjectives'
		self.basic = "offensive"
		self.jsondata = {}
