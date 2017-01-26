

from xai.brain.wordbase.nouns._singular import _SINGULAR

#calss header
class _SINGULARS(_SINGULAR, ):
	def __init__(self,): 
		_SINGULAR.__init__(self)
		self.name = "SINGULARS"
		self.specie = 'nouns'
		self.basic = "singular"
		self.jsondata = {}
