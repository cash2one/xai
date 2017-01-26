

from xai.brain.wordbase.verbs._configure import _CONFIGURE

#calss header
class _CONFIGURED(_CONFIGURE, ):
	def __init__(self,): 
		_CONFIGURE.__init__(self)
		self.name = "CONFIGURED"
		self.specie = 'verbs'
		self.basic = "configure"
		self.jsondata = {}
