

from xai.brain.wordbase.nouns._spar import _SPAR

#calss header
class _SPARS(_SPAR, ):
	def __init__(self,): 
		_SPAR.__init__(self)
		self.name = "SPARS"
		self.specie = 'nouns'
		self.basic = "spar"
		self.jsondata = {}
