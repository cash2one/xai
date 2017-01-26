

from xai.brain.wordbase.verbs._assert import _ASSERT

#calss header
class _ASSERTS(_ASSERT, ):
	def __init__(self,): 
		_ASSERT.__init__(self)
		self.name = "ASSERTS"
		self.specie = 'verbs'
		self.basic = "assert"
		self.jsondata = {}
