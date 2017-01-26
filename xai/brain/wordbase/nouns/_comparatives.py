

from xai.brain.wordbase.nouns._comparative import _COMPARATIVE

#calss header
class _COMPARATIVES(_COMPARATIVE, ):
	def __init__(self,): 
		_COMPARATIVE.__init__(self)
		self.name = "COMPARATIVES"
		self.specie = 'nouns'
		self.basic = "comparative"
		self.jsondata = {}
