

from xai.brain.wordbase.nouns._cloak import _CLOAK

#calss header
class _CLOAKED(_CLOAK, ):
	def __init__(self,): 
		_CLOAK.__init__(self)
		self.name = "CLOAKED"
		self.specie = 'nouns'
		self.basic = "cloak"
		self.jsondata = {}
