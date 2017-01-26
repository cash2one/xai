

from xai.brain.wordbase.verbs._stump import _STUMP

#calss header
class _STUMPS(_STUMP, ):
	def __init__(self,): 
		_STUMP.__init__(self)
		self.name = "STUMPS"
		self.specie = 'verbs'
		self.basic = "stump"
		self.jsondata = {}
