

from xai.brain.wordbase.verbs._complement import _COMPLEMENT

#calss header
class _COMPLEMENTED(_COMPLEMENT, ):
	def __init__(self,): 
		_COMPLEMENT.__init__(self)
		self.name = "COMPLEMENTED"
		self.specie = 'verbs'
		self.basic = "complement"
		self.jsondata = {}
