

from xai.brain.wordbase.verbs._reschedule import _RESCHEDULE

#calss header
class _RESCHEDULED(_RESCHEDULE, ):
	def __init__(self,): 
		_RESCHEDULE.__init__(self)
		self.name = "RESCHEDULED"
		self.specie = 'verbs'
		self.basic = "reschedule"
		self.jsondata = {}
