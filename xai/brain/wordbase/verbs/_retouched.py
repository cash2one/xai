

from xai.brain.wordbase.verbs._retouch import _RETOUCH

#calss header
class _RETOUCHED(_RETOUCH, ):
	def __init__(self,): 
		_RETOUCH.__init__(self)
		self.name = "RETOUCHED"
		self.specie = 'verbs'
		self.basic = "retouch"
		self.jsondata = {}
