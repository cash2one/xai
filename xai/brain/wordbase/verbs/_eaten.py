

from xai.brain.wordbase.verbs._eat import _EAT

#calss header
class _EATEN(_EAT, ):
	def __init__(self,): 
		_EAT.__init__(self)
		self.name = "EATEN"
		self.specie = 'verbs'
		self.basic = "eat"
		self.jsondata = {}
