

from xai.brain.wordbase.verbs._idle import _IDLE

#calss header
class _IDLING(_IDLE, ):
	def __init__(self,): 
		_IDLE.__init__(self)
		self.name = "IDLING"
		self.specie = 'verbs'
		self.basic = "idle"
		self.jsondata = {}
