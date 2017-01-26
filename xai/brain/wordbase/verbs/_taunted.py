

from xai.brain.wordbase.verbs._taunt import _TAUNT

#calss header
class _TAUNTED(_TAUNT, ):
	def __init__(self,): 
		_TAUNT.__init__(self)
		self.name = "TAUNTED"
		self.specie = 'verbs'
		self.basic = "taunt"
		self.jsondata = {}
