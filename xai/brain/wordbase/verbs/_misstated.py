

from xai.brain.wordbase.verbs._misstate import _MISSTATE

#calss header
class _MISSTATED(_MISSTATE, ):
	def __init__(self,): 
		_MISSTATE.__init__(self)
		self.name = "MISSTATED"
		self.specie = 'verbs'
		self.basic = "misstate"
		self.jsondata = {}
