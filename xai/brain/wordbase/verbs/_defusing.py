

from xai.brain.wordbase.verbs._defuse import _DEFUSE

#calss header
class _DEFUSING(_DEFUSE, ):
	def __init__(self,): 
		_DEFUSE.__init__(self)
		self.name = "DEFUSING"
		self.specie = 'verbs'
		self.basic = "defuse"
		self.jsondata = {}
