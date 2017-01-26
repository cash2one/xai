

from xai.brain.wordbase.verbs._examine import _EXAMINE

#calss header
class _EXAMINED(_EXAMINE, ):
	def __init__(self,): 
		_EXAMINE.__init__(self)
		self.name = "EXAMINED"
		self.specie = 'verbs'
		self.basic = "examine"
		self.jsondata = {}
