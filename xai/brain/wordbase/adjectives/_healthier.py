

from xai.brain.wordbase.adjectives._healthy import _HEALTHY

#calss header
class _HEALTHIER(_HEALTHY, ):
	def __init__(self,): 
		_HEALTHY.__init__(self)
		self.name = "HEALTHIER"
		self.specie = 'adjectives'
		self.basic = "healthy"
		self.jsondata = {}
