

from xai.brain.wordbase.verbs._heal import _HEAL

#calss header
class _HEALS(_HEAL, ):
	def __init__(self,): 
		_HEAL.__init__(self)
		self.name = "HEALS"
		self.specie = 'verbs'
		self.basic = "heal"
		self.jsondata = {}
