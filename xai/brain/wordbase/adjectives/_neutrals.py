

from xai.brain.wordbase.adjectives._neutral import _NEUTRAL

#calss header
class _NEUTRALS(_NEUTRAL, ):
	def __init__(self,): 
		_NEUTRAL.__init__(self)
		self.name = "NEUTRALS"
		self.specie = 'adjectives'
		self.basic = "neutral"
		self.jsondata = {}
