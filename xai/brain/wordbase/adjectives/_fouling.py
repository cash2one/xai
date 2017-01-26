

from xai.brain.wordbase.adjectives._foul import _FOUL

#calss header
class _FOULING(_FOUL, ):
	def __init__(self,): 
		_FOUL.__init__(self)
		self.name = "FOULING"
		self.specie = 'adjectives'
		self.basic = "foul"
		self.jsondata = {}
