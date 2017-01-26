

from xai.brain.wordbase.verbs._wrench import _WRENCH

#calss header
class _WRENCHES(_WRENCH, ):
	def __init__(self,): 
		_WRENCH.__init__(self)
		self.name = "WRENCHES"
		self.specie = 'verbs'
		self.basic = "wrench"
		self.jsondata = {}
