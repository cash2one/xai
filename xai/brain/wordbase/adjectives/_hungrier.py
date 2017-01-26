

from xai.brain.wordbase.adjectives._hungry import _HUNGRY

#calss header
class _HUNGRIER(_HUNGRY, ):
	def __init__(self,): 
		_HUNGRY.__init__(self)
		self.name = "HUNGRIER"
		self.specie = 'adjectives'
		self.basic = "hungry"
		self.jsondata = {}
