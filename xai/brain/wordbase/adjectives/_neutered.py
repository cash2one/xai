

from xai.brain.wordbase.adjectives._neuter import _NEUTER

#calss header
class _NEUTERED(_NEUTER, ):
	def __init__(self,): 
		_NEUTER.__init__(self)
		self.name = "NEUTERED"
		self.specie = 'adjectives'
		self.basic = "neuter"
		self.jsondata = {}
