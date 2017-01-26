

from xai.brain.wordbase.adjectives._singular import _SINGULAR

#calss header
class _SINGULARS(_SINGULAR, ):
	def __init__(self,): 
		_SINGULAR.__init__(self)
		self.name = "SINGULARS"
		self.specie = 'adjectives'
		self.basic = "singular"
		self.jsondata = {}
