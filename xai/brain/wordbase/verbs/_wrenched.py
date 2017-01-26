

from xai.brain.wordbase.verbs._wrench import _WRENCH

#calss header
class _WRENCHED(_WRENCH, ):
	def __init__(self,): 
		_WRENCH.__init__(self)
		self.name = "WRENCHED"
		self.specie = 'verbs'
		self.basic = "wrench"
		self.jsondata = {}
