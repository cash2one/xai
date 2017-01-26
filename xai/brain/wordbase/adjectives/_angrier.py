

from xai.brain.wordbase.adjectives._angry import _ANGRY

#calss header
class _ANGRIER(_ANGRY, ):
	def __init__(self,): 
		_ANGRY.__init__(self)
		self.name = "ANGRIER"
		self.specie = 'adjectives'
		self.basic = "angry"
		self.jsondata = {}
