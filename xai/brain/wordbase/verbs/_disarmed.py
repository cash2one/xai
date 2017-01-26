

from xai.brain.wordbase.verbs._disarm import _DISARM

#calss header
class _DISARMED(_DISARM, ):
	def __init__(self,): 
		_DISARM.__init__(self)
		self.name = "DISARMED"
		self.specie = 'verbs'
		self.basic = "disarm"
		self.jsondata = {}
