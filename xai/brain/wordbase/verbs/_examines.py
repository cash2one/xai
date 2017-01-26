

from xai.brain.wordbase.verbs._examine import _EXAMINE

#calss header
class _EXAMINES(_EXAMINE, ):
	def __init__(self,): 
		_EXAMINE.__init__(self)
		self.name = "EXAMINES"
		self.specie = 'verbs'
		self.basic = "examine"
		self.jsondata = {}
