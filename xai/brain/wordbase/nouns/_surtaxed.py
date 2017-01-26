

from xai.brain.wordbase.nouns._surtax import _SURTAX

#calss header
class _SURTAXED(_SURTAX, ):
	def __init__(self,): 
		_SURTAX.__init__(self)
		self.name = "SURTAXED"
		self.specie = 'nouns'
		self.basic = "surtax"
		self.jsondata = {}
