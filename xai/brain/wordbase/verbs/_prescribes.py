

from xai.brain.wordbase.verbs._prescribe import _PRESCRIBE

#calss header
class _PRESCRIBES(_PRESCRIBE, ):
	def __init__(self,): 
		_PRESCRIBE.__init__(self)
		self.name = "PRESCRIBES"
		self.specie = 'verbs'
		self.basic = "prescribe"
		self.jsondata = {}
