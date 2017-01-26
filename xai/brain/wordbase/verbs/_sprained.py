

from xai.brain.wordbase.verbs._sprain import _SPRAIN

#calss header
class _SPRAINED(_SPRAIN, ):
	def __init__(self,): 
		_SPRAIN.__init__(self)
		self.name = "SPRAINED"
		self.specie = 'verbs'
		self.basic = "sprain"
		self.jsondata = {}
