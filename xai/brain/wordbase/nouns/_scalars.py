

from xai.brain.wordbase.nouns._scalar import _SCALAR

#calss header
class _SCALARS(_SCALAR, ):
	def __init__(self,): 
		_SCALAR.__init__(self)
		self.name = "SCALARS"
		self.specie = 'nouns'
		self.basic = "scalar"
		self.jsondata = {}
