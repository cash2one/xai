

from xai.brain.wordbase.adjectives._sexist import _SEXIST

#calss header
class _SEXISTS(_SEXIST, ):
	def __init__(self,): 
		_SEXIST.__init__(self)
		self.name = "SEXISTS"
		self.specie = 'adjectives'
		self.basic = "sexist"
		self.jsondata = {}
