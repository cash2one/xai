

from xai.brain.wordbase.verbs._possess import _POSSESS

#calss header
class _POSSESSING(_POSSESS, ):
	def __init__(self,): 
		_POSSESS.__init__(self)
		self.name = "POSSESSING"
		self.specie = 'verbs'
		self.basic = "possess"
		self.jsondata = {}
