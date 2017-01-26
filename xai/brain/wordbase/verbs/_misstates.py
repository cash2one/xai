

from xai.brain.wordbase.verbs._misstate import _MISSTATE

#calss header
class _MISSTATES(_MISSTATE, ):
	def __init__(self,): 
		_MISSTATE.__init__(self)
		self.name = "MISSTATES"
		self.specie = 'verbs'
		self.basic = "misstate"
		self.jsondata = {}
