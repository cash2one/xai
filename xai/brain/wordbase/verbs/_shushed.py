

from xai.brain.wordbase.verbs._shush import _SHUSH

#calss header
class _SHUSHED(_SHUSH, ):
	def __init__(self,): 
		_SHUSH.__init__(self)
		self.name = "SHUSHED"
		self.specie = 'verbs'
		self.basic = "shush"
		self.jsondata = {}
