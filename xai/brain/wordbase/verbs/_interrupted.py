

from xai.brain.wordbase.verbs._interrupt import _INTERRUPT

#calss header
class _INTERRUPTED(_INTERRUPT, ):
	def __init__(self,): 
		_INTERRUPT.__init__(self)
		self.name = "INTERRUPTED"
		self.specie = 'verbs'
		self.basic = "interrupt"
		self.jsondata = {}
