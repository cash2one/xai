

from xai.brain.wordbase.adjectives._rare import _RARE

#calss header
class _RARER(_RARE, ):
	def __init__(self,): 
		_RARE.__init__(self)
		self.name = "RARER"
		self.specie = 'adjectives'
		self.basic = "rare"
		self.jsondata = {}
