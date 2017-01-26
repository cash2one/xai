

from xai.brain.wordbase.verbs._simulate import _SIMULATE

#calss header
class _SIMULATED(_SIMULATE, ):
	def __init__(self,): 
		_SIMULATE.__init__(self)
		self.name = "SIMULATED"
		self.specie = 'verbs'
		self.basic = "simulate"
		self.jsondata = {}
