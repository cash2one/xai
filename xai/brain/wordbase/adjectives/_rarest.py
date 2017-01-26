

from xai.brain.wordbase.adjectives._rare import _RARE

#calss header
class _RAREST(_RARE, ):
	def __init__(self,): 
		_RARE.__init__(self)
		self.name = "RAREST"
		self.specie = 'adjectives'
		self.basic = "rare"
		self.jsondata = {}
