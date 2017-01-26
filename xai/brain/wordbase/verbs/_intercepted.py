

from xai.brain.wordbase.verbs._intercept import _INTERCEPT

#calss header
class _INTERCEPTED(_INTERCEPT, ):
	def __init__(self,): 
		_INTERCEPT.__init__(self)
		self.name = "INTERCEPTED"
		self.specie = 'verbs'
		self.basic = "intercept"
		self.jsondata = {}
