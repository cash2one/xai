

from xai.brain.wordbase.adjectives._positive import _POSITIVE

#calss header
class _POSITIVES(_POSITIVE, ):
	def __init__(self,): 
		_POSITIVE.__init__(self)
		self.name = "POSITIVES"
		self.specie = 'adjectives'
		self.basic = "positive"
		self.jsondata = {}
