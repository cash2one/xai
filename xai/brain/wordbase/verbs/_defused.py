

from xai.brain.wordbase.verbs._defuse import _DEFUSE

#calss header
class _DEFUSED(_DEFUSE, ):
	def __init__(self,): 
		_DEFUSE.__init__(self)
		self.name = "DEFUSED"
		self.specie = 'verbs'
		self.basic = "defuse"
		self.jsondata = {}
