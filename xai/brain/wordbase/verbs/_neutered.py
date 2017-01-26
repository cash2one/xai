

from xai.brain.wordbase.verbs._neuter import _NEUTER

#calss header
class _NEUTERED(_NEUTER, ):
	def __init__(self,): 
		_NEUTER.__init__(self)
		self.name = "NEUTERED"
		self.specie = 'verbs'
		self.basic = "neuter"
		self.jsondata = {}
