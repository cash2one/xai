

from xai.brain.wordbase.verbs._nudge import _NUDGE

#calss header
class _NUDGED(_NUDGE, ):
	def __init__(self,): 
		_NUDGE.__init__(self)
		self.name = "NUDGED"
		self.specie = 'verbs'
		self.basic = "nudge"
		self.jsondata = {}
