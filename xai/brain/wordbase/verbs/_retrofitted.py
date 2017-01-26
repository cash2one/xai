

from xai.brain.wordbase.verbs._retrofit import _RETROFIT

#calss header
class _RETROFITTED(_RETROFIT, ):
	def __init__(self,): 
		_RETROFIT.__init__(self)
		self.name = "RETROFITTED"
		self.specie = 'verbs'
		self.basic = "retrofit"
		self.jsondata = {}
