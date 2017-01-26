

from xai.brain.wordbase.nouns._prior import _PRIOR

#calss header
class _PRIORS(_PRIOR, ):
	def __init__(self,): 
		_PRIOR.__init__(self)
		self.name = "PRIORS"
		self.specie = 'nouns'
		self.basic = "prior"
		self.jsondata = {}
