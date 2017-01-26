

from xai.brain.wordbase.nouns._neutral import _NEUTRAL

#calss header
class _NEUTRALS(_NEUTRAL, ):
	def __init__(self,): 
		_NEUTRAL.__init__(self)
		self.name = "NEUTRALS"
		self.specie = 'nouns'
		self.basic = "neutral"
		self.jsondata = {}
