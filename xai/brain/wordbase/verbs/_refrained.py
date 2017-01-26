

from xai.brain.wordbase.verbs._refrain import _REFRAIN

#calss header
class _REFRAINED(_REFRAIN, ):
	def __init__(self,): 
		_REFRAIN.__init__(self)
		self.name = "REFRAINED"
		self.specie = 'verbs'
		self.basic = "refrain"
		self.jsondata = {}
