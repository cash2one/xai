

from xai.brain.wordbase.verbs._alert import _ALERT

#calss header
class _ALERTED(_ALERT, ):
	def __init__(self,): 
		_ALERT.__init__(self)
		self.name = "ALERTED"
		self.specie = 'verbs'
		self.basic = "alert"
		self.jsondata = {}
