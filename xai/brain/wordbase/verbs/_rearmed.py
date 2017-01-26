

from xai.brain.wordbase.verbs._rearm import _REARM

#calss header
class _REARMED(_REARM, ):
	def __init__(self,): 
		_REARM.__init__(self)
		self.name = "REARMED"
		self.specie = 'verbs'
		self.basic = "rearm"
		self.jsondata = {}
