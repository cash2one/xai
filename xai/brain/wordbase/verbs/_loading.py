

from xai.brain.wordbase.verbs._load import _LOAD

#calss header
class _LOADING(_LOAD, ):
	def __init__(self,): 
		_LOAD.__init__(self)
		self.name = "LOADING"
		self.specie = 'verbs'
		self.basic = "load"
		self.jsondata = {}
