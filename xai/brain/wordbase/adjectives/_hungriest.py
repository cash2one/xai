

from xai.brain.wordbase.adjectives._hungry import _HUNGRY

#calss header
class _HUNGRIEST(_HUNGRY, ):
	def __init__(self,): 
		_HUNGRY.__init__(self)
		self.name = "HUNGRIEST"
		self.specie = 'adjectives'
		self.basic = "hungry"
		self.jsondata = {}
