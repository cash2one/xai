

from xai.brain.wordbase.adjectives._broadcast import _BROADCAST

#calss header
class _BROADCASTED(_BROADCAST, ):
	def __init__(self,): 
		_BROADCAST.__init__(self)
		self.name = "BROADCASTED"
		self.specie = 'adjectives'
		self.basic = "broadcast"
		self.jsondata = {}
