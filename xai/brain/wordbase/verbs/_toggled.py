

from xai.brain.wordbase.verbs._toggle import _TOGGLE

#calss header
class _TOGGLED(_TOGGLE, ):
	def __init__(self,): 
		_TOGGLE.__init__(self)
		self.name = "TOGGLED"
		self.specie = 'verbs'
		self.basic = "toggle"
		self.jsondata = {}
