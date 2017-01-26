

from xai.brain.wordbase.exclamations._shush import _SHUSH

#calss header
class _SHUSHED(_SHUSH, ):
	def __init__(self,): 
		_SHUSH.__init__(self)
		self.name = "SHUSHED"
		self.specie = 'exclamations'
		self.basic = "shush"
		self.jsondata = {}
