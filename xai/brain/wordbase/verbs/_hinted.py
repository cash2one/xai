

from xai.brain.wordbase.verbs._hint import _HINT

#calss header
class _HINTED(_HINT, ):
	def __init__(self,): 
		_HINT.__init__(self)
		self.name = "HINTED"
		self.specie = 'verbs'
		self.basic = "hint"
		self.jsondata = {}
