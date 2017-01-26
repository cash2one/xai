

from xai.brain.wordbase.verbs._rewire import _REWIRE

#calss header
class _REWIRED(_REWIRE, ):
	def __init__(self,): 
		_REWIRE.__init__(self)
		self.name = "REWIRED"
		self.specie = 'verbs'
		self.basic = "rewire"
		self.jsondata = {}
