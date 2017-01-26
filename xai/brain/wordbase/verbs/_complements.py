

from xai.brain.wordbase.verbs._complement import _COMPLEMENT

#calss header
class _COMPLEMENTS(_COMPLEMENT, ):
	def __init__(self,): 
		_COMPLEMENT.__init__(self)
		self.name = "COMPLEMENTS"
		self.specie = 'verbs'
		self.basic = "complement"
		self.jsondata = {}
