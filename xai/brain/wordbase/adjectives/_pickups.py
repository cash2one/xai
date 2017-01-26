

from xai.brain.wordbase.adjectives._pickup import _PICKUP

#calss header
class _PICKUPS(_PICKUP, ):
	def __init__(self,): 
		_PICKUP.__init__(self)
		self.name = "PICKUPS"
		self.specie = 'adjectives'
		self.basic = "pickup"
		self.jsondata = {}
