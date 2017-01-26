

from xai.brain.wordbase.verbs._warn import _WARN

#calss header
class _WARNED(_WARN, ):
	def __init__(self,): 
		_WARN.__init__(self)
		self.name = "WARNED"
		self.specie = 'verbs'
		self.basic = "warn"
		self.jsondata = {}
