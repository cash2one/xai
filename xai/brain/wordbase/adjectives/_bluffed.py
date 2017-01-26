

from xai.brain.wordbase.adjectives._bluff import _BLUFF

#calss header
class _BLUFFED(_BLUFF, ):
	def __init__(self,): 
		_BLUFF.__init__(self)
		self.name = "BLUFFED"
		self.specie = 'adjectives'
		self.basic = "bluff"
		self.jsondata = {}
