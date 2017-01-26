

from xai.brain.wordbase.verbs._inject import _INJECT

#calss header
class _INJECTED(_INJECT, ):
	def __init__(self,): 
		_INJECT.__init__(self)
		self.name = "INJECTED"
		self.specie = 'verbs'
		self.basic = "inject"
		self.jsondata = {}
