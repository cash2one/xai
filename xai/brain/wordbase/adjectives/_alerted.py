

from xai.brain.wordbase.adjectives._alert import _ALERT

#calss header
class _ALERTED(_ALERT, ):
	def __init__(self,): 
		_ALERT.__init__(self)
		self.name = "ALERTED"
		self.specie = 'adjectives'
		self.basic = "alert"
		self.jsondata = {}
