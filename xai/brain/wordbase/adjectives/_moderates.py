

from xai.brain.wordbase.adjectives._moderate import _MODERATE

#calss header
class _MODERATES(_MODERATE, ):
	def __init__(self,): 
		_MODERATE.__init__(self)
		self.name = "MODERATES"
		self.specie = 'adjectives'
		self.basic = "moderate"
		self.jsondata = {}
