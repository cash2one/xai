

from xai.brain.wordbase.verbs._load import _LOAD

#calss header
class _LOADS(_LOAD, ):
	def __init__(self,): 
		_LOAD.__init__(self)
		self.name = "LOADS"
		self.specie = 'verbs'
		self.basic = "load"
		self.jsondata = {}
