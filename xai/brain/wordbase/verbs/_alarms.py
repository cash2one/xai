

from xai.brain.wordbase.verbs._alarm import _ALARM

#calss header
class _ALARMS(_ALARM, ):
	def __init__(self,): 
		_ALARM.__init__(self)
		self.name = "ALARMS"
		self.specie = 'verbs'
		self.basic = "alarm"
		self.jsondata = {}
