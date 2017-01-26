

from xai.brain.wordbase.verbs._persist import _PERSIST

#calss header
class _PERSISTED(_PERSIST, ):
	def __init__(self,): 
		_PERSIST.__init__(self)
		self.name = "PERSISTED"
		self.specie = 'verbs'
		self.basic = "persist"
		self.jsondata = {}
