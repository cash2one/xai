

from xai.brain.wordbase.adjectives._crude import _CRUDE

#calss header
class _CRUDER(_CRUDE, ):
	def __init__(self,): 
		_CRUDE.__init__(self)
		self.name = "CRUDER"
		self.specie = 'adjectives'
		self.basic = "crude"
		self.jsondata = {}
