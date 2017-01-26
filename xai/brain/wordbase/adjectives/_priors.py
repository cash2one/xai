

from xai.brain.wordbase.adjectives._prior import _PRIOR

#calss header
class _PRIORS(_PRIOR, ):
	def __init__(self,): 
		_PRIOR.__init__(self)
		self.name = "PRIORS"
		self.specie = 'adjectives'
		self.basic = "prior"
		self.jsondata = {}
