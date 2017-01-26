

from xai.brain.wordbase.verbs._cloak import _CLOAK

#calss header
class _CLOAKED(_CLOAK, ):
	def __init__(self,): 
		_CLOAK.__init__(self)
		self.name = "CLOAKED"
		self.specie = 'verbs'
		self.basic = "cloak"
		self.jsondata = {}
