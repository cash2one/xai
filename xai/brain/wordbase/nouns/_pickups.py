

from xai.brain.wordbase.nouns._pickup import _PICKUP

#calss header
class _PICKUPS(_PICKUP, ):
	def __init__(self,): 
		_PICKUP.__init__(self)
		self.name = "PICKUPS"
		self.specie = 'nouns'
		self.basic = "pickup"
		self.jsondata = {}
