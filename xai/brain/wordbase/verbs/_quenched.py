

from xai.brain.wordbase.verbs._quench import _QUENCH

#calss header
class _QUENCHED(_QUENCH, ):
	def __init__(self,): 
		_QUENCH.__init__(self)
		self.name = "QUENCHED"
		self.specie = 'verbs'
		self.basic = "quench"
		self.jsondata = {}
