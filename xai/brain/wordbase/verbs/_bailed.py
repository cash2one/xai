

from xai.brain.wordbase.verbs._bail import _BAIL

#calss header
class _BAILED(_BAIL, ):
	def __init__(self,): 
		_BAIL.__init__(self)
		self.name = "BAILED"
		self.specie = 'verbs'
		self.basic = "bail"
		self.jsondata = {}
