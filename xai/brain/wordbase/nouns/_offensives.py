

from xai.brain.wordbase.nouns._offensive import _OFFENSIVE

#calss header
class _OFFENSIVES(_OFFENSIVE, ):
	def __init__(self,): 
		_OFFENSIVE.__init__(self)
		self.name = "OFFENSIVES"
		self.specie = 'nouns'
		self.basic = "offensive"
		self.jsondata = {}
